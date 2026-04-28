# Job Class Synthesis: Comparison Matrix

> Claude (inline, 15 classes) vs. Opus 4.6 via API (16 classes)

## Strong matches — same class, same scope

| Claude (inline) | Opus 4.6 (API) | Notes |
|---|---|---|
| 1. Collections Intern / Digitization Intern | 16. Intern / Entry-Level Trainee | Match |
| 3. Archivist / Project Archivist | 11. Archivist / Librarian | Match |
| 4. Curatorial / Collections Associate (PhD) | 3. Curatorial Associate | Match |
| 10. Senior CM / Director of Collections | 9. Director / VP of Collections | Match |
| 11. Curator (Tenure-Track / Research) | 5. Research Curator / Faculty Curator | Match |
| 15. Postdoc (Biodiversity Informatics) | 12. Postdoc (Biodiversity Informatics) | Match |

## Splits and merges — same data, different grouping

| Claude (inline) | Opus 4.6 (API) | Notes |
|---|---|---|
| 2. Curatorial / Museum Technician | 2. Museum Specialist / Curatorial Asst | Opus split by discipline |
| *(merged into #2)* | 15. Herbarium Curatorial Asst / Tech | Opus split by discipline |
| 5. Collections Manager | 1. Collections Manager | Match |
| 6. Herbarium Curator / CM (Botany) | *(folded into #1 and #15)* | Claude split by discipline; Opus merged |
| 7. Digitization Manager / Supervisor | 14. Digitization Project Manager | Opus split by seniority |
| *(merged into #7)* | 8. Digitization Technician / Specialist | Opus split by seniority |
| 8. Biodiversity Informatics Specialist | 7. Software Developer / Engineer | Opus split by function |
| *(merged into #8)* | 13. Biodiversity Data Analyst / Scientist | Opus split by function |
| 9. CM / Curator (Researcher-Track) | *(absorbed into #1 and #5)* | Claude created hybrid class; Opus distributed |
| 12. Collections Info Mgr / DB Admin | 6. Collections Informatics Mgr / DB Mgr | Match |
| 13. Biodiversity Informatics Mgr / Director | *(folded into #9 Director)* | Claude split by seniority; Opus merged |
| 14. VP Collections & Research | *(folded into #9 Director)* | Claude split by seniority; Opus merged |

## Unique to one version

| Claude (inline) | Opus 4.6 (API) | Notes |
|---|---|---|
| *(no equivalent)* | 4. Assistant Collections Manager | New class in Opus |
| *(no equivalent)* | 10. Registrar | New class in Opus |

# Claude (inline) adds...

This is a really interesting comparison. Let me lay out where the two versions converge and diverge. Here's how the two versions stack up: I identified 15 classes, Opus 4.6 identified 16. Both arrived at the same core taxonomy — the 8 strong matches at the top of the chart cover the same roles with the same boundaries. The differences are all about where to lump vs. split.

## Where Opus split what I merged

The biggest divergence is in digitization and informatics. I created single umbrella classes for "Digitization Manager / Digitization Supervisor" and "Biodiversity Informatics Specialist" — Opus carved those into four separate classes (Digitization Technician, Digitization Project Manager, Software Developer, and Data Analyst/Scientist). Opus's approach is arguably better here; the skill sets and career trajectories of a $17/hr digitization intern and a $70K project manager coordinating a 19-institution NSF network are different enough to warrant separate profiles. Same logic for the difference between someone writing Symbiota code and someone running R analyses on community science data.

Similarly, I lumped all herbarium technician-type roles into my general "Curatorial / Museum Technician" class. Opus broke out a dedicated "Herbarium Curatorial Assistant / Technician" class, which makes sense given how many herbarium-specific postings are in the dataset and how different the daily work is from zoological collections.

## Where I split what Opus merged

I maintained three separate senior leadership tiers — VP of Collections & Research, Biodiversity Informatics Director, and Senior Collections Manager / Director of Collections. Opus consolidated all of those into a single "Director of Collections / VP" class. My approach gives more granularity to the difference between an operational collections director (Carnegie's DCCA) and a research-leadership role (Drexel's VP), but Opus's consolidation is defensible given how few postings exist at that level.

I also carved out a dedicated "Herbarium Curator / Collections Manager (Botany-Specific)" class and a hybrid "Collections Manager / Curator (Researcher-Track)" class. Opus folded the botany-specific roles into the general Collections Manager and Herbarium Technician classes, and distributed researcher-track positions between Collections Manager and Research Curator. This is a reasonable simplification.

## What Opus caught that I missed

Opus identified two classes I didn't break out separately: **Assistant Collections Manager** (DMNS, NHMLA, Stanford — a distinct mid-tier role between technician and collections manager) and **Registrar** (NHMLA, Canadian Museum of Nature — a specialized documentation/compliance role). Both are legitimate and well-represented in the data. The Registrar omission in particular is a gap in my version.

## Where the insights align

Both versions flagged the same cross-cutting patterns: salary compression, the grant-funding instability problem, the growing informatics imperative across all roles, and the strong effect of employer type on compensation. Opus's "Cross-Cutting Observations" section is more concise than my embedded commentary but covers the same ground. Opus also added a nice employer-type breakdown at the end that ranks institution categories by compensation — a useful addition.

## Quality of prose

Both are thorough and well-organized. Opus's version is about 50% longer (1,260 vs 849 lines), mostly because of its more granular splitting and more detailed salary breakdowns with specific institutional examples. My version has slightly more narrative texture in the descriptions (I editorialize a bit more about what roles feel like in practice), while Opus is more systematic and reference-oriented.

## Bottom line

If I were advising someone entering this field, I'd probably hand them the Opus version — the finer-grained class structure is more useful for career navigation, and the Registrar and Assistant Collections Manager classes fill real gaps. But both arrive at fundamentally the same picture of the field.