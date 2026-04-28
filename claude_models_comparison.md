

<h2 class="sr-only">Comparison of job classes identified by Claude (inline) vs Opus 4.6 (API)</h2>
<style>
.row{display:grid;grid-template-columns:minmax(0,1fr) 40px minmax(0,1fr);gap:0;align-items:stretch;border-bottom:0.5px solid var(--color-border-tertiary);min-height:44px}
.row:last-child{border-bottom:none}
.cell{padding:8px 12px;font-size:13px;color:var(--color-text-primary);display:flex;align-items:center}
.cell.l{justify-content:flex-end;text-align:right}
.cell.r{justify-content:flex-start;text-align:left}
.link{display:flex;align-items:center;justify-content:center;font-size:16px}
.hdr{font-weight:500;font-size:14px;color:var(--color-text-secondary);padding:6px 12px;border-bottom:0.5px solid var(--color-border-secondary)}
.hdr.l{text-align:right}
.badge{display:inline-block;padding:2px 8px;border-radius:var(--border-radius-md);font-size:11px;font-weight:500;margin-left:6px;vertical-align:middle}
.badge.new{background:var(--color-background-info);color:var(--color-text-info)}
.badge.split{background:var(--color-background-warning);color:var(--color-text-warning)}
.badge.same{background:var(--color-background-success);color:var(--color-text-success)}
.badge.merged{background:#EEEDFE;color:#534AB7}
.section{padding:10px 12px;font-size:12px;font-weight:500;color:var(--color-text-secondary);text-transform:uppercase;letter-spacing:0.5px;background:var(--color-background-secondary);grid-column:1/-1}
.num{color:var(--color-text-tertiary);font-size:12px;min-width:18px;display:inline-block}
</style>

<div style="padding:1rem 0">

<div style="display:grid;grid-template-columns:minmax(0,1fr) 40px minmax(0,1fr);gap:0;margin-bottom:2px">
<div class="hdr l">Claude (inline) — 15 classes</div>
<div class="hdr" style="text-align:center"></div>
<div class="hdr">Opus 4.6 (API) — 16 classes</div>
</div>

<div class="section">Strong matches — same class, same scope</div>

<div class="row">
<div class="cell l"><span class="num">1.</span> Collections Intern / Digitization Intern</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">16.</span> Intern / Entry-Level Trainee <span class="badge same">match</span></div>
</div>
<div class="row">
<div class="cell l"><span class="num">3.</span> Archivist / Project Archivist</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">11.</span> Archivist / Librarian <span class="badge same">match</span></div>
</div>
<div class="row">
<div class="cell l"><span class="num">4.</span> Curatorial / Collections Associate (PhD)</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">3.</span> Curatorial Associate <span class="badge same">match</span></div>
</div>
<div class="row">
<div class="cell l"><span class="num">10.</span> Senior CM / Director of Collections</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">9.</span> Director / VP of Collections <span class="badge same">match</span></div>
</div>
<div class="row">
<div class="cell l"><span class="num">11.</span> Curator (Tenure-Track / Research)</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">5.</span> Research Curator / Faculty Curator <span class="badge same">match</span></div>
</div>
<div class="row">
<div class="cell l"><span class="num">15.</span> Postdoc (Biodiversity Informatics)</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">12.</span> Postdoc (Biodiversity Informatics) <span class="badge same">match</span></div>
</div>

<div class="section">Splits and merges — same data, different grouping</div>

<div class="row">
<div class="cell l"><span class="num">2.</span> Curatorial / Museum Technician</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">2.</span> Museum Specialist / Curatorial Asst <span class="badge split">split</span></div>
</div>
<div class="row">
<div class="cell l" style="color:var(--color-text-tertiary);font-style:italic">(merged into #2)</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">15.</span> Herbarium Curatorial Asst / Tech <span class="badge split">split</span></div>
</div>

<div class="row">
<div class="cell l"><span class="num">5.</span> Collections Manager</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">1.</span> Collections Manager <span class="badge same">match</span></div>
</div>

<div class="row">
<div class="cell l"><span class="num">6.</span> Herbarium Curator / CM (Botany)</div>
<div class="link">↔</div>
<div class="cell r" style="color:var(--color-text-tertiary);font-style:italic">(folded into #1 and #15) <span class="badge merged">merged</span></div>
</div>

<div class="row">
<div class="cell l"><span class="num">7.</span> Digitization Manager / Supervisor</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">14.</span> Digitization Project Manager <span class="badge split">split</span></div>
</div>
<div class="row">
<div class="cell l" style="color:var(--color-text-tertiary);font-style:italic">(merged into #7)</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">8.</span> Digitization Technician / Specialist <span class="badge split">split</span></div>
</div>

<div class="row">
<div class="cell l"><span class="num">8.</span> Biodiversity Informatics Specialist</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">7.</span> Software Developer / Engineer <span class="badge split">split</span></div>
</div>
<div class="row">
<div class="cell l" style="color:var(--color-text-tertiary);font-style:italic">(merged into #8)</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">13.</span> Biodiversity Data Analyst / Scientist <span class="badge split">split</span></div>
</div>

<div class="row">
<div class="cell l"><span class="num">9.</span> CM / Curator (Researcher-Track)</div>
<div class="link">↔</div>
<div class="cell r" style="color:var(--color-text-tertiary);font-style:italic">(absorbed into #1 and #5) <span class="badge merged">merged</span></div>
</div>

<div class="row">
<div class="cell l"><span class="num">12.</span> Collections Info Mgr / DB Admin</div>
<div class="link">↔</div>
<div class="cell r"><span class="num">6.</span> Collections Informatics Mgr / DB Mgr <span class="badge same">match</span></div>
</div>
<div class="row">
<div class="cell l"><span class="num">13.</span> Biodiversity Informatics Mgr / Director</div>
<div class="link">↔</div>
<div class="cell r" style="color:var(--color-text-tertiary);font-style:italic">(folded into #9 Director) <span class="badge merged">merged</span></div>
</div>
<div class="row">
<div class="cell l"><span class="num">14.</span> VP Collections & Research</div>
<div class="link">↔</div>
<div class="cell r" style="color:var(--color-text-tertiary);font-style:italic">(folded into #9 Director) <span class="badge merged">merged</span></div>
</div>

<div class="section">Unique to one version</div>

<div class="row">
<div class="cell l" style="color:var(--color-text-tertiary);font-style:italic">(no equivalent)</div>
<div class="link"></div>
<div class="cell r"><span class="num">4.</span> Assistant Collections Manager <span class="badge new">new</span></div>
</div>
<div class="row">
<div class="cell l" style="color:var(--color-text-tertiary);font-style:italic">(no equivalent)</div>
<div class="link"></div>
<div class="cell r"><span class="num">10.</span> Registrar <span class="badge new">new</span></div>
</div>

</div>
This is a really interesting comparison. Let me lay out where the two versions converge and diverge.Here's how the two versions stack up:

**Overall structure:** I identified 15 classes, Opus 4.6 identified 16. Both arrived at the same core taxonomy — the 8 strong matches at the top of the chart cover the same roles with the same boundaries. The differences are all about where to lump vs. split.

**Where Opus split what I merged:**

The biggest divergence is in digitization and informatics. I created single umbrella classes for "Digitization Manager / Digitization Supervisor" and "Biodiversity Informatics Specialist" — Opus carved those into four separate classes (Digitization Technician, Digitization Project Manager, Software Developer, and Data Analyst/Scientist). Opus's approach is arguably better here; the skill sets and career trajectories of a $17/hr digitization intern and a $70K project manager coordinating a 19-institution NSF network are different enough to warrant separate profiles. Same logic for the difference between someone writing Symbiota code and someone running R analyses on community science data.

Similarly, I lumped all herbarium technician-type roles into my general "Curatorial / Museum Technician" class. Opus broke out a dedicated "Herbarium Curatorial Assistant / Technician" class, which makes sense given how many herbarium-specific postings are in the dataset and how different the daily work is from zoological collections.

**Where I split what Opus merged:**

I maintained three separate senior leadership tiers — VP of Collections & Research, Biodiversity Informatics Director, and Senior Collections Manager / Director of Collections. Opus consolidated all of those into a single "Director of Collections / VP" class. My approach gives more granularity to the difference between an operational collections director (Carnegie's DCCA) and a research-leadership role (Drexel's VP), but Opus's consolidation is defensible given how few postings exist at that level.

I also carved out a dedicated "Herbarium Curator / Collections Manager (Botany-Specific)" class and a hybrid "Collections Manager / Curator (Researcher-Track)" class. Opus folded the botany-specific roles into the general Collections Manager and Herbarium Technician classes, and distributed researcher-track positions between Collections Manager and Research Curator. This is a reasonable simplification.

**What Opus caught that I missed:**

Opus identified two classes I didn't break out separately: **Assistant Collections Manager** (DMNS, NHMLA, Stanford — a distinct mid-tier role between technician and collections manager) and **Registrar** (NHMLA, Canadian Museum of Nature — a specialized documentation/compliance role). Both are legitimate and well-represented in the data. The Registrar omission in particular is a gap in my version.

**Where the insights align:**

Both versions flagged the same cross-cutting patterns: salary compression, the grant-funding instability problem, the growing informatics imperative across all roles, and the strong effect of employer type on compensation. Opus's "Cross-Cutting Observations" section is more concise than my embedded commentary but covers the same ground. Opus also added a nice employer-type breakdown at the end that ranks institution categories by compensation — a useful addition.

**Quality of prose:** Both are thorough and well-organized. Opus's version is about 50% longer (1,260 vs 849 lines), mostly because of its more granular splitting and more detailed salary breakdowns with specific institutional examples. My version has slightly more narrative texture in the descriptions (I editorialize a bit more about what roles feel like in practice), while Opus is more systematic and reference-oriented.

**Bottom line:** If I were advising someone entering this field, I'd probably hand them the Opus version — the finer-grained class structure is more useful for career navigation, and the Registrar and Assistant Collections Manager classes fill real gaps. But both arrive at fundamentally the same picture of the field.