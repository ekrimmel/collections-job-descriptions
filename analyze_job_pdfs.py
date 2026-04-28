#!/usr/bin/env python3
"""
Job Description PDF Analyzer
Extracts structured data from job description PDFs using the Claude API.
Outputs a single CSV with one row per PDF.

Requirements:
    pip install anthropic

Usage:
    1. Set your API key:  export ANTHROPIC_API_KEY="sk-ant-..."
    2. Run:               python analyze_job_pdfs.py --folder /path/to/pdfs
    3. Output:            job_descriptions.csv (in current directory)

Default behavior:
    - If the output CSV already exists, new files are APPENDED and already-processed
      files are skipped automatically (safe to re-run with new PDFs at any time)
    - A timestamped backup of the existing CSV is created before any run that would
      modify it, e.g. job_descriptions_backup_20260428_143022.csv

Optional flags:
    --output my_file.csv      Custom output filename
    --workers 3               Parallel workers (default: 3, be mindful of rate limits)
    --overwrite               Reprocess ALL files and overwrite the output CSV
                              (a backup is still created before overwriting)
"""

import anthropic
import argparse
import base64
import csv
import json
import os
import shutil
import sys
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ── Fields to extract ────────────────────────────────────────────────────────

FIELDS = [
    "title",
    "classification",
    "employer",
    "location",
    "employment_type",
    "salary_compensation",
    "experience",
    "required_education",
    "date_closed",
    "date_other",
    "description",
    "duties",
    "required_skills_qualifications",
    "desired_skills_qualifications",
    "required_physical",
    "benefits",
]

FIELD_DESCRIPTIONS = {
    "title":
        "The working/functional title of the job as it would commonly be known (e.g. 'Biological Scientist', 'Park Ranger'). Do NOT use the civil service classification title here.",
    "classification":
        "For US federal or state government jobs only: the official civil service classification title or pay grade, such as 'OPS F&W BIOLOGICAL SCIENTIST II' or 'GS-12'. If both a classification title and a grade/level are present, include both. Use 'Not specified' for non-government jobs or government jobs where this information is absent.",
    "employer":
        "The hiring company or agency name",
    "location":
        "City/state/country and whether remote, hybrid, or on-site",
    "employment_type":
        "e.g. Full-time, Part-time, Contract, Internship",
    "salary_compensation":
        "Salary range or compensation details as stated",
    "experience":
        "Required or preferred years of experience",
    "required_education":
        "Degree or certification requirements",
    "date_closed":
        "The explicit date the job posting closed or expired, only if directly stated in the document. Use ISO format YYYY-MM-DD. If not explicitly stated, use 'Not specified' and populate date_other instead.",
    "date_other":
        "If date_job_closed is 'Not specified', make your best guess at when the job closed based on any dates present in the document (e.g. posting date, application deadline, document metadata). Use ISO format YYYY-MM-DD and briefly note the basis for the guess in parentheses, e.g. '2024-03-15 (estimated from posting date)'. If date_job_closed is known, leave this as 'Not specified'.",
    "description":
        "A high-level summary or overview of the role if one is present in the document. Copy verbatim where possible.",
    "duties":
        "The responsibilities and day-to-day tasks of the role. Copy verbatim from the document wherever possible. Join multiple items with ' | '.",
    "required_skills_qualifications":
        "Skills, knowledge, competencies, and qualifications that are explicitly required. Copy verbatim from the document wherever possible. Exclude administrative requirements like background checks, drug tests, or eligibility paperwork. Join multiple items with ' | '.",
    "desired_skills_qualifications":
        "Skills or qualifications listed as preferred, desired, a plus, or 'nice to have' — only if the document makes a clear distinction from required. Copy verbatim wherever possible. Join multiple items with ' | '. If no such distinction is made, use 'Not specified'.",
    "required_physical":
        "Any physical demands of the role, such as lifting weight limits, standing duration, mobility requirements, or sensory requirements. Copy verbatim wherever possible. Join multiple items with ' | '.",
    "benefits":
        "Non-financial benefits offered, such as health insurance, PTO, retirement plans, flexible schedules, professional development, or other perks. Exclude salary and cash compensation. Join multiple items with ' | '.",
}

# ── Claude prompt ─────────────────────────────────────────────────────────────

def build_prompt():
    field_lines = "\n".join(
        f'  "{f}": "{FIELD_DESCRIPTIONS[f]}"' for f in FIELDS
    )
    return f"""You are a data extraction assistant. Analyze this job description PDF and extract the following fields.

Fields to extract:
{field_lines}

Rules:
- Return ONLY a valid JSON object with exactly these keys: {json.dumps(FIELDS)}
- If a field is not found or unclear, use the string "Not specified"
- Do not include any explanation, markdown, or text outside the JSON object
- For duties, required_skills_qualifications, desired_skills_qualifications, required_physical, and benefits: copy text verbatim from the document wherever possible, joining multiple items with " | "
- For required_skills_qualifications: exclude administrative/legal requirements such as background checks, drug tests, I-9 eligibility, or driving record checks
- For title: use the working/functional title only — never the civil service classification string
- For classification: only populate for US federal or state government postings; include both the classification title and pay grade/series if both are present
- For date_closed: only use a date explicitly stated as a closing/expiration date; otherwise use "Not specified" and populate date_other
- For date_other: if date_closed is "Not specified", estimate from any available dates and note the basis in parentheses
- For salary_compensation: include currency symbol and range if present (e.g. "$90,000 - $120,000/yr")
- For benefits: exclude salary, bonuses, and financial compensation — focus on non-financial perks and benefits"""

# ── Core extraction function ──────────────────────────────────────────────────

def extract_from_pdf(pdf_path: Path, client: anthropic.Anthropic, retries: int = 3) -> dict:
    """Send a PDF to Claude and return extracted fields as a dict."""
    with open(pdf_path, "rb") as f:
        pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

    for attempt in range(retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=4000,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": build_prompt(),
                            },
                        ],
                    }
                ],
            )

            raw = response.content[0].text.strip()
            # Strip markdown fences if the model adds them despite instructions
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            extracted = json.loads(raw.strip())

            # Ensure all fields are present
            for field in FIELDS:
                if field not in extracted:
                    extracted[field] = "Not specified"

            extracted["source_file"] = pdf_path.name
            extracted["status"] = "ok"
            return extracted

        except json.JSONDecodeError as e:
            print(f"  ⚠  JSON parse error for {pdf_path.name} (attempt {attempt+1}): {e}")
        except anthropic.RateLimitError:
            wait = 2 ** attempt * 5
            print(f"  ⏳ Rate limit hit — waiting {wait}s before retry...")
            time.sleep(wait)
        except Exception as e:
            print(f"  ✗  Error processing {pdf_path.name} (attempt {attempt+1}): {e}")
            if attempt == retries - 1:
                break
            time.sleep(2)

    # Return a failure row so the file is still represented in the CSV
    return {
        "source_file": pdf_path.name,
        "status": "error",
        **{field: "Error" for field in FIELDS},
    }

# ── CSV helpers ───────────────────────────────────────────────────────────────

CSV_COLUMNS = ["source_file", "status"] + FIELDS

def load_already_processed(output_path: Path) -> set:
    """Return set of filenames already in the output CSV (for --resume)."""
    if not output_path.exists():
        return set()
    with open(output_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {row["source_file"] for row in reader if "source_file" in row}

def write_rows(output_path: Path, rows: list[dict], append: bool = False):
    mode = "a" if append else "w"
    write_header = not append or not output_path.exists()
    with open(output_path, mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        if write_header:
            writer.writeheader()
        writer.writerows(rows)

def backup_csv(output_path: Path) -> Path | None:
    """Copy existing CSV to a timestamped backup file. Returns backup path or None."""
    if not output_path.exists():
        return None
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    stem = output_path.stem
    backup_path = output_path.with_name(f"{stem}_backup_{timestamp}.csv")
    shutil.copy2(output_path, backup_path)
    return backup_path



def main():
    parser = argparse.ArgumentParser(description="Batch-analyze job description PDFs with Claude.")
    parser.add_argument("--folder",    required=True, help="Path to folder containing PDFs")
    parser.add_argument("--output",    default="job_descriptions.csv", help="Output CSV filename")
    parser.add_argument("--workers",   type=int, default=3, help="Parallel workers (default: 3)")
    parser.add_argument("--overwrite", action="store_true", help="Reprocess ALL files and overwrite output CSV (a backup is still made)")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.")
        sys.exit(1)

    pdf_files = sorted(folder.glob("*.pdf")) + sorted(folder.glob("*.PDF"))
    if not pdf_files:
        print(f"No PDF files found in '{folder}'.")
        sys.exit(0)

    output_path = Path(args.output)

    # Always back up an existing CSV before doing anything that touches it
    if output_path.exists():
        backup_path = backup_csv(output_path)
        print(f"Backup created: {backup_path}")

    # Default: append new files only. --overwrite reprocesses everything.
    already_done = set()
    if not args.overwrite:
        already_done = load_already_processed(output_path)
        if already_done:
            print(f"Resuming — skipping {len(already_done)} already-processed file(s).")

    to_process = [p for p in pdf_files if p.name not in already_done]
    total = len(to_process)
    print(f"Found {len(pdf_files)} PDF(s) — processing {total}.\n")

    if total == 0:
        print("Nothing new to process. Use --overwrite to reprocess all files.")
        sys.exit(0)

    completed = 0
    errors = 0

    # On --overwrite start fresh; otherwise append to existing CSV
    first_write = args.overwrite

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_path = {
            executor.submit(extract_from_pdf, pdf, client): pdf
            for pdf in to_process
        }
        for future in as_completed(future_to_path):
            pdf_path = future_to_path[future]
            try:
                result = future.result()
            except Exception as e:
                result = {
                    "source_file": pdf_path.name,
                    "status": f"exception: {e}",
                    **{field: "Error" for field in FIELDS},
                }

            completed += 1
            status_icon = "✓" if result["status"] == "ok" else "✗"
            print(f"  [{completed}/{total}] {status_icon}  {pdf_path.name}")
            if result["status"] != "ok":
                errors += 1

            write_rows(output_path, [result], append=not first_write)
            first_write = False  # subsequent writes always append

    print(f"\nDone! {completed - errors}/{total} succeeded, {errors} errors.")
    print(f"Output saved to: {output_path.resolve()}")

if __name__ == "__main__":
    main()
