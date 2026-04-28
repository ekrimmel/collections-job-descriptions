#!/usr/bin/env python3
"""
Job Class Synthesizer
Reads a CSV of extracted job descriptions and sends it to Claude Opus 4.6
to produce a synthesized markdown document of job classes.

Requirements:
    pip install anthropic

Usage:
    1. Set your API key:  export ANTHROPIC_API_KEY="sk-ant-..."
    2. Run:               python synthesize_job_classes.py --input job_descriptions.csv
    3. Output:            job_class_synthesis.md (in current directory)

Optional flags:
    --output my_file.md   Custom output filename
"""

import anthropic
import argparse
import os
import sys
from pathlib import Path

SYSTEM_PROMPT = """You are an expert labor market analyst specializing in natural history museum collections, \
biodiversity informatics, and related fields. You have deep knowledge of civil service classification \
systems (federal GS grades, state pay bands), museum professional organizations (SPNHC, AAM), \
and the operational realities of managing natural history collections at institutions of all sizes."""

SYNTHESIS_PROMPT = """Below is a CSV containing data extracted from several hundred job description PDFs. \
Each row represents a single job posting from a natural history museum, university herbarium or museum, \
botanical garden, government agency, or related institution. The data spans approximately 2016–2026.

Your task is to analyze ALL rows and synthesize them into a set of coherent **job classes** — groups of \
positions that share enough in common to be described as a single archetypal role. You should identify \
as many distinct classes as the data supports (expect roughly 10–20). For each class, produce the \
following sections:

## [Class Name]

### Equivalent Classifications
If relevant, map to US federal (e.g., GS-12) and/or state government official civil service \
classification titles or pay grades observed in the data for this class.

### Type of Employer
Big-picture description of where these jobs are found (e.g., freestanding museum, academic position \
at a university museum, state government agency, botanical garden, etc.)

### Salary
Range observed in US dollars, with notes on what drives variation.

### Experience
Required or preferred years of experience.

### Education
Degree or certification requirements.

---

### Description
A high-level summary of the role — what it is, what it exists to do, and how it fits into the \
organizational structure of a natural history institution.

### Duties
The responsibilities and day-to-day tasks of the role, formatted as a bulleted list. Synthesize \
across postings to capture the full scope of what someone in this class would typically do.

### Required Skills and Qualifications
Skills, knowledge, competencies, and qualifications that are expected to be required across \
postings in this class. Formatted as a bulleted list.

### Desired Skills and Qualifications
Skills and qualifications that are expected to be desired but not strictly required. Formatted \
as a bulleted list.

### Physical Requirements
Any physical demands of the role (lifting, standing, climbing, chemical exposure, fieldwork, etc.). \
Synthesize the range observed across postings.

### Benefits
Non-financial benefits commonly offered (health insurance, PTO, retirement, tuition, professional \
development, etc.). Exclude salary and cash compensation.

---

Additional guidelines:
- Base your synthesis entirely on the data provided. Do not invent categories or details that \
  are not represented in the CSV.
- When salary data uses non-USD currencies (CAD, AUD, GBP), note this and provide approximate \
  USD equivalents.
- Note patterns and insights that emerge from the data (e.g., salary compression, career track \
  divergences, differences between employer types).
- Exclude rows where status = "error" from your analysis.
- Write the output as a well-structured markdown document with a title, brief introduction, \
  and then the job class profiles.
- Be thorough — the document should be comprehensive enough to serve as a reference for someone \
  entering or navigating this career field.

Here is the CSV data:

"""


def main():
    parser = argparse.ArgumentParser(
        description="Synthesize job classes from extracted job description CSV using Claude Opus 4.6."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the job_descriptions.csv file",
    )
    parser.add_argument(
        "--output",
        default="job_class_synthesis.md",
        help="Output markdown filename (default: job_class_synthesis.md)",
    )
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: '{input_path}' not found.")
        sys.exit(1)

    csv_text = input_path.read_text(encoding="utf-8")
    row_count = csv_text.count("\n") - 1  # subtract header
    print(f"Loaded {input_path.name}: {row_count} rows, {len(csv_text):,} characters")

    # Rough token estimate (1 token ≈ 4 chars for English text)
    approx_tokens = len(csv_text) // 4
    approx_cost_input = (approx_tokens / 1_000_000) * 5  # Opus input: $5/M tokens
    approx_cost_output = (16_000 / 1_000_000) * 25       # Opus output: $25/M tokens, estimate 16K output
    print(f"Estimated input: ~{approx_tokens:,} tokens")
    print(f"Estimated cost:  ~${approx_cost_input + approx_cost_output:.2f}")
    print()

    confirm = input("Proceed? [y/N] ").strip().lower()
    if confirm not in ("y", "yes"):
        print("Cancelled.")
        sys.exit(0)

    client = anthropic.Anthropic(api_key=api_key)

    print("\nSending to Claude Opus 4.6 — this may take a few minutes...")
    print("(The model is reading and synthesizing all rows at once.)\n")

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": SYNTHESIS_PROMPT + csv_text,
            }
        ],
    )

    output_text = response.content[0].text

    output_path = Path(args.output)
    output_path.write_text(output_text, encoding="utf-8")

    # Print usage stats
    usage = response.usage
    actual_cost_input = (usage.input_tokens / 1_000_000) * 5
    actual_cost_output = (usage.output_tokens / 1_000_000) * 25
    actual_cost_total = actual_cost_input + actual_cost_output

    print(f"Done! Output saved to: {output_path.resolve()}")
    print(f"\nAPI usage:")
    print(f"  Input tokens:  {usage.input_tokens:,}")
    print(f"  Output tokens: {usage.output_tokens:,}")
    print(f"  Actual cost:   ~${actual_cost_total:.2f}")


if __name__ == "__main__":
    main()
