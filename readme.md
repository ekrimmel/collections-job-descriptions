# Jobs in Biodiversity Collections (Data) Management

For the past decade or so, I have been saving [PDFs of job postings](/data) for positions working (mostly) in or around biodiversity collections, e.g. in natural history museums or at university-based collections. I asked Claude to help transcribe, parse, and synthesis this dataset of 249 postings. For $24.02 ($11 of which was me making one dumb mistake) and 3 hours of my time (with me starting at zero, asking Claude to tell me how to ask Claude to do the thing), I got:

1. A nice CSV of every job posting with data transcribed and parsed: [job_descriptions.csv](job_descriptions.csv)
1. Two syntheses of how the data above translate into more generic job classes: one using Claude's [Sonnet 4.6 model](job_class_synthesis_sonnet4-6.md) and the other using the premium [Opus 4.6 model](job_class_synthesis_opus4-6.md)
1. A comparison of the two syntheses: [claude_models_comparison.md](claude_models_comparison.md)

Claude also had some high-level thoughts that sum it all up in a nutshell:

> The dataset divides naturally into two major career tracks — collections stewardship (entries 1–11) and biodiversity informatics/technology (entries 8, 12–15) — with significant overlap at the middle levels where data management skills are increasingly expected of collections professionals.
> A few patterns worth noting across the dataset: salary compression is severe at the lower end (entry-level collections work in the $35,000–$50,000 range despite often requiring a Master's degree), government positions (Smithsonian GS-13, Florida FWC, NC DNCR) offer some of the clearest salary transparency and most competitive compensation relative to educational requirements, and the informatics track tends to pay better at all levels than the pure collections track for comparable seniority.

Please feel free to re-use or add to this dataset and its products! If you want me to add a job posting here, check that it doesn't already exist (in [job_descriptions.csv](job_descriptions.csv)) and then share a PDF with me by filing a GitHub issue in this repo.
