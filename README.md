
# Orbital Debris Assessment: Tracking Growth and Risk in Low Earth Orbit

**Author:** James Glosser  
**Contact:** [Email](mailto:DemonicUrges05@gmail.com) | [LinkedIn profile](https://www.linkedin.com/in/james-glosser-249100204/)  
**Repository:** [GitHub repository](https://github.com/sithid/orbital-debris-assessment)  
**Last Updated:** April 2026  
**Status:** Final submission with all outputs included for review. The repository contains a full pipeline refresh, including all executed notebooks, cleaned datasets, query outputs, and visuals as of the final analysis state.

---

## Project Overview

This capstone investigates the accelerating growth and evolving risks in low Earth orbit (LEO), focusing on the dramatic shift from steady, linear expansion to an era of exponential object proliferation since 2014. Using a structured, reproducible pipeline, the project cleans and merges authoritative satellite and debris catalogs, synthesizes a physics-informed master dataset, and normalizes it into a relational SQLite database. Targeted queries and visual analyses reveal when orbital growth took off, where high-risk objects are concentrated, and which organizations are most responsible for non-operational “zombie” satellites. The analysis is grounded in transparent, query-driven methods and physics-based risk metrics, providing a clear view of how and why congestion and collision hazards are intensifying.

## Main Research Questions

**Primary Questions:**

- When did orbital growth shift from a linear to an exponential trend?
- Where are high-risk objects (by mass and kinetic energy) most concentrated, especially in the crowded 400–600 km LEO region?
- Which organizations or operators are most responsible for non-operational (“zombie”) satellites?

**Secondary Questions:**

- How do object type (PAYLOAD, ROCKET BODY, DEBRIS) and operational status relate to kinetic risk in orbit?
- Do user categories (commercial, government, military, civil) show distinct risk profiles in terms of congestion and kinetic risk?

**Additional Insights (Miscellaneous):**

- How has the total mass launched, decayed, and remaining in orbit changed over time?
- How is the total mass in orbit distributed across different orbit classes?
- What is the joint distribution of object mass and another variable (e.g., altitude, year)?
- What is the age distribution of satellites currently in orbit?
- Which countries have the most objects in orbit?
- What were the largest single launch events in terms of number of objects or mass?
- Which events contributed the most debris to the orbital environment?

## Summary of Findings

**2014 marks the inflection point**: Orbital growth transitions from linear to exponential, driven by commercial megaconstellations, reusable rockets, and satellite miniaturization.
**High-risk objects are overwhelmingly concentrated in LEO**, especially in the 400–600 km band, which is now the epicenter of congestion and collision risk.
**Responsibility for non-operational satellites is highly concentrated**: A small number of organizations and contractors account for most “zombie” payloads, while commercial operators now dominate both active and inactive satellite populations.
**Kinetic risk is driven by large, uncontrolled objects**—especially dead payloads, spent rocket bodies, and the largest debris fragments. Most debris is small, but a few massive pieces pose catastrophic risk.
**User category matters**: Commercial satellites are most numerous, but government and military payloads are much heavier and longer-lived, carrying outsized kinetic risk. Civil satellites are generally low-risk, while “unknown” objects add uncertainty.
**Total mass in orbit continues to grow**: The mass of objects launched, decayed, and remaining in orbit shows persistent accumulation, with most mass concentrated in LEO and specific orbital classes.
**Aging and legacy objects persist**: The age distribution of satellites reveals a growing population of “zombie” and legacy objects, many of which remain in orbit for decades.
**National and event-driven contributions are significant**: A handful of countries and major launch or fragmentation events account for a disproportionate share of objects and debris in orbit.
**Effective risk reduction requires targeted action**: Improved end-of-life practices, stricter disposal requirements, and focused cleanup among the biggest contributors are essential for a safer, more sustainable orbital environment.

### Current Workflow

The analysis pipeline is organized into sequential notebooks, each handling a specific stage of the project. There is also a utility notebook for viewing documentation.

0. **Markdown Viewer Utility**  
   `notebooks/00_markdown_viewer.ipynb` — View markdown documentation in Jupyter.

1. **Pipeline Refresh**  
   `notebooks/00_pipeline_refresh.ipynb` — Download original datasets.

2. **UCS Cleanup**  
   `notebooks/01_ucs_cleanup.ipynb` — Standardize and validate the UCS satellite registry.

3. **SATCAT Cleanup and Reconstruction**  
   `notebooks/02_satcat_cleanup.ipynb` — Clean the SATCAT catalog and repair missing values.

4. **Master Synthesis**  
   `notebooks/03_kinetic_master_synthesis.ipynb` — Merge cleaned sources into the master dataset.

5. **SQLite Normalization**  
   `notebooks/04_orbital_debris_synthesis.ipynb` — Convert the master dataset into a normalized SQLite database.

6. **Orbital Debris Exploration**  
   `notebooks/05_orbital_debris_exploration.ipynb` — Run queries and generate outputs for the final story.

7. **Story Narrative**  
   `notebooks/06_orbital_debris_story.ipynb` — Present answers and visuals for the main research questions.

### Repository Structure

```bash
orbital-debris-assessment/
|- charts/                        # question-driven figures (by type/phase)
|- data/
|  |- original/                   # raw source files (satcat.csv, UCS-Satellite-Database.csv, etc.)
|  \- clean/                      # cleaned CSVs, SQLite database, parquet query outputs
|     |- kinetic_master.csv
|     |- satcat_cleaned.csv
|     |- ucs_cleaned.csv
|     |- orbital_debris.db
|     \- results/                 # compact query outputs (parquet)
|- docs/                          # capstone proposal, data dictionaries, and supporting docs
|  |- archive/
      | - 00_analysis_scatchpad.ipynb
      | - Capstone Project Proposal - James Glosser.md
      | - Orbital Debris Exploration Checklist.md
|  |- resources/
|  \- schema/
|- images/                        # exported figures and schema image
|- notebooks/                     # stepwise analysis pipeline and utilities
|  |- 00_markdown_viewer.ipynb    # utility: view markdown docs in Jupyter
|  |- 00_pipeline_refresh.ipynb
|  |- 01_ucs_cleanup.ipynb
|  |- 02_satcat_cleanup.ipynb
|  |- 03_kinetic_master_synthesis.ipynb
|  |- 04_orbital_debris_synthesis.ipynb
|  |- 05_orbital_debris_exploration.ipynb
|  |- 06_orbital_debris_story.ipynb
|  |- execute.py
|  |- utility.py
|- README.md
\- requirements.txt
```

### Key Data Products

| Artifact                        | Description                              | Size/Details                |
|----------------------------------|------------------------------------------|-----------------------------|
| `data/clean/ucs_cleaned.csv`     | Cleaned UCS satellite registry           | 7,542 rows × 34 columns     |
| `data/clean/satcat_cleaned.csv`  | Cleaned SATCAT global catalog            | 68,400 rows × 27 columns    |
| `data/clean/kinetic_master.csv`  | Merged, physics-informed master dataset  | 68,400 rows × 48 columns    |
| `data/clean/orbital_debris.db`   | Normalized SQLite analysis database      | 6 tables (see below)        |
| `data/clean/results/*.parquet`   | Query outputs for all visualizations     | Varies by query             |

The SQLite database includes these tables:

- `satellites`
- `orbital_data`
- `ucs_details`
- `risk_assessment`
- `ownership_operators`
- `launch_events`

### Data Sources

- **CelesTrak Satellite Catalog (SATCAT):**  
   Baseline global catalog for payloads, rocket bodies, and debris.  
   [http://celestrak.org/pub/satcat.csv](http://celestrak.org/pub/satcat.csv)

- **UCS Satellite Database:**  
   Higher-fidelity payload metadata (ownership, mission, launch mass, lifetime).  
   [http://www.ucsusa.org/resources/satellite-database](http://www.ucsusa.org/resources/satellite-database)

- **ESA Space Environment Report 2025:**  
   External benchmark for assumptions, validation, and proxy reasoning.  
   [https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf](https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf)

### Usage & Reproduction

All output artifacts are included from a full pipeline refresh, so every query result, visualization, and analysis matches the final project state. Reviewers can verify the narrative, figures, and conclusions directly—no reruns or regeneration needed.

**Why include all outputs?**

- Ensures analysis and visuals are reproducible and match the documented story, regardless of future data or package changes.
- Allows reviewers to audit, review, or reuse results without running the pipeline.
- Preserves the exact state of the project as submitted.

**Quick review:**  
To review the final story and results, install dependencies and open `notebooks/output/06_orbital_debris_story_executed.ipynb`. All supporting outputs and data are included.

### Installation & Environment Setup

```bash
# Clone the repository
git clone https://github.com/sithid/orbital-debris-assessment.git
cd orbital-debris-assessment

# Create and activate virtual environment (REQUIRED)
python -m venv venv

# Activate virtual environment:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Pipeline Execution

To fully reproduce or update the outputs, run the pipeline from the `notebooks/` directory using the CLI options below. This will regenerate all outputs, but is not required for review unless you wish to update or extend the analysis.

**Warning:** Running `--first-run`, `--refresh`, or `--purge` will delete existing outputs and datasets. Use with caution if you want to preserve the current state.  Run only execute.py --vis-only to regenerate visuals without affecting datasets.

```bash
cd notebooks

# First run: downloads original datasets, purges outputs, runs the full pipeline
python execute.py --first-run

# Standard run: uses existing datasets, runs the full pipeline
python execute.py

# Refresh datasets and rerun pipeline
python execute.py --refresh

# Purge outputs and rerun pipeline
python execute.py --purge

# Purge outputs only, do not rerun pipeline
python execute.py --purge-only

# Data-only: rerun only data cleaning/synthesis (notebooks 01-04)
python execute.py --data-only

# Vis-only: rerun only exploration/query/visualization/presentation notebooks (notebooks 05-08)
python execute.py --vis-only
```

**Flag Interaction Notes:**  

- `--first-run` always runs the full pipeline with purge and refresh, ignoring other flags.
- `--vis-only` with `--purge` ignores purge to avoid deleting required data.
- Using both `--vis-only` and `--data-only` runs the full pipeline.

**Refresh Usage:**  
CelesTrak allows ~10 refreshes per day. Use `--refresh` sparingly to avoid throttling.

### Output & Documentation Review

- Review executed notebooks in `notebooks` for the full analysis narrative, including all outputs and visuals.
- For a summary, see `06_orbital_debris_story.ipynb`.
- To view documentation in Jupyter, use `00_markdown_viewer.ipynb`.

**Recommended Workflow:**  
This project is designed for reproducible, stepwise analysis—no manual notebook editing required. The recommended workflow is:

1. **Set up your environment** (one-time)
2. **Run the pipeline** with a single command
3. **Review outputs** Review executed notebook cell outputs or use the markdown viewer for documentation

**Manual Execution:**  
You may run each notebook in order for full control (see notebook list above), but the CLI is recommended for reproducibility.

- Use the `execute.py` command to run the pipeline and generate outputs.
- Review results in the original notebooks after pipeline execution.
- Use the markdown viewer notebook for in-notebook documentation access / review.
- Manual notebook execution is possible but not recommended for typical use.

### Assumptions and Limitations

- SATCAT and UCS do not provide identical coverage, so matching quality depends on shared identifiers and metadata consistency.
- Some physics and mass fields require imputation or derivation rather than direct observation.
- The SQLite layer improves reproducibility, but it does not eliminate source-era gaps or historical catalog inconsistencies.
- High-risk summary tables can contain missing average values where a group exists but no object in that group qualifies as high risk.

### Why This Structure Matters

The old flat-file-centered workflow made it too easy to mix cleaning, modeling, querying, and storytelling in the same place. The current structure separates those concerns:

- cleaned source registries for repeatable preprocessing
- a master synthesis layer for feature engineering
- a normalized SQLite database for structured analysis
- query outputs that freeze the logic for each research question
- a visualization notebook that focuses only on presentation

### AI Usage & Authorship Note

AI assistance (primarily GitHub Copilot) was utilized as a development tool for formula and function development, error debugging, documentation/markdown tone, and research. AI-assisted functions are explicitly identified in their respective headers.

**Human Authorship & Governance**  
I retain full authorship and responsibility for the following core components:

- **Strategic Framework:** Research direction, conceptual framing, and methodology.
- **Data Architecture:** All data-cleaning logic, schema definitions, and pipeline design.
- **Analytical Logic:** Query structure, data interpretation, and final conclusions.
- **Critical Judgment:** Final assumptions and technical tradeoff decisions.

**Verification & Accountability**  
All AI-generated suggestions underwent rigorous manual review, verification, and editing prior to usage in any way. I remain fully accountable for the accuracy, integrity, and logic of the completed work in its entirety.
