# WORK IN PROGRESS

This readme is a work in progress and is not intended as the complete/final version of the document.  This readme will be considered final at the time I turn it in for grading, or on April 10th, 2026, whichever comes first.

## Orbital Debris Assessment: Mapping the Kessler Acceleration in Low Earth Orbit  

**Author:** James Glosser  
**Contact:** [Email](mailto:DemonicUrges05@gmail.com) | [LinkedIn profile](https://www.linkedin.com/in/james-glosser-249100204/)  
**Repository:** [GitHub repository](https://github.com/sithid/orbital-debris-assessment)  
**Last Updated:** March 2026  
**Status:** Code:You Capstone Project #4 (Data Analysis Pathway), updated to reflect the current notebook -> SQLite -> query -> visualization workflow.

---

### Project Overview

This capstone examines whether low Earth orbit is entering a more dangerous growth regime driven by rapid satellite deployment, persistent rocket bodies, and long-lived debris. The project started as a flat-file workflow centered on `kinetic_master.csv`, but the current structure is more deliberate: clean the source datasets, synthesize a physics-informed master registry, normalize that registry into SQLite, run focused analytical queries, and generate final visualizations from compact query outputs.

The goal is not just to count objects in orbit. It is to identify when orbital growth shifts from a historical linear pattern into a modern acceleration regime, and to map where the highest-risk objects are concentrating by orbit class, altitude band, and object type.

### Research Questions

#### Primary Questions

- At what year did orbital growth decouple from a historical linear trend and transition into an exponential trajectory?
- How are high-risk objects, measured through velocity and kinetic energy, distributed across orbit classes and altitude bands, especially in the 400-600 km LEO band?
- Which ownership or operator groups contribute most to non-operational zombie payload concentrations?

#### Secondary Questions

- How do launch cohorts and post-2014 deployment patterns affect congestion intensity?
- How do object type and operational status relate to kinetic risk?
- Do user categories such as commercial, government, military, and civil show distinct risk profiles?

### Current Workflow

The repo is organized as a staged analysis pipeline. Each notebook handles a distinct phase of the project. There is also a utility notebook for documentation viewing.

**See the 'Recommended Usage & Output Review' section below for how to review outputs and documentation.**

0. **Markdown Viewer Utility**  
   `notebooks/00_markdown_viewer.ipynb` is a utility notebook for interactively viewing and rendering markdown files (such as documentation or proposals) within Jupyter. It is not part of the main data pipeline, but is useful for reviewing project documentation directly in the notebook interface.

1. **Pipeline Refresh**  
   `notebooks/00_pipeline_refresh.ipynb.ipynb` downloads original datasets from their respective sources.

2. **UCS cleanup**  
   `notebooks/01_ucs_cleanup.ipynb` standardizes and validates the UCS satellite registry, producing `data/clean/ucs_cleaned.csv`.

3. **SATCAT cleanup and reconstruction**  
   `notebooks/02_satcat_cleanup.ipynb` cleans the SATCAT catalog, repairs missing orbital values, and exports `data/clean/satcat_cleaned.csv`.

4. **Master synthesis**  
   `notebooks/03_kinetic_master_synthesis.ipynb` merges the cleaned sources into the physics-informed master dataset `data/clean/kinetic_master.csv`.

5. **SQLite normalization**  
   `notebooks/04_orbital_debris_synthesis.ipynb` converts the master dataset into a normalized SQLite database at `data/clean/orbital_debris.db`.

6. **Orbital Debris exploration**  
   `notebooks/05_orbital_debris_exploration.ipynb` runs exploratory queries and visuals to explore the sql database thoroughly.

7. **Story questions**  
   `notebooks/06_orbital_debris_queries.ipynb` runs project question queries against the SQLite database and exports compact parquet result sets to `data/clean/queries/`.

8. **Visualization layer**  
   `notebooks/07_orbital_debris_visualizations.ipynb` reads the query outputs and generates the final figures in `images/`.

9. **Presentation layer**  
   `notebooks/08_orbital_debris_assessment_presentation.ipynb` provides the final project presentation, summarizing key findings, visuals, and conclusions for review or sharing.

### Repository Structure

```text
orbital-debris-assessment/
|- charts/                        # question-driven figures (by type/phase)
|  \- questions/
|     |- exploratory/
|     |   |- png/
|     |   \- svg/
|     |- primary/
|     |   |- png/
|     |   \- svg/
|     \- secondary/
|         |- png/
|         \- svg/
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
|  |- misc/
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
|  |- 06_orbital_debris_story_queries.ipynb
|  |- 07_orbital_debris_story_visualizations.ipynb
|  |- 08_orbital_debris_assessment_presentation.ipynb
|  |- execute.py
|  |- output/                     # executed notebooks with outputs
|  \- utility.py
|- README.md
\- requirements.txt
```

### Key Data Products

| Artifact | Current Role | Size |
| --- | --- | --- |
| `data/clean/ucs_cleaned.csv` | Cleaned UCS satellite registry | 7,542 rows x 34 columns |
| `data/clean/satcat_cleaned.csv` | Cleaned SATCAT global catalog | 68,087 rows x 27 columns |
| `data/clean/kinetic_master.csv` | Physics-informed synthesized master dataset | 33,234 rows x 47 columns |
| `data/clean/orbital_debris.db` | Normalized SQLite analysis database | 6 relational tables |
| `data/clean/results/*.parquet` | Compact query results for all queries used in any visualization | Dependent On Query |

The SQLite database currently contains these tables:

- `satellites`
- `orbital_data`
- `ucs_details`
- `risk_assessment`
- `ownership_operators`
- `launch_events`

### Data Sources

#### 1. CelesTrak Satellite Catalog (SATCAT)

- **Source:** CelesTrak / U.S. Space Command (USSPACECOM)
- **Use in this project:** baseline global object catalog for payloads, rocket bodies, and debris
- **Link:** [http://celestrak.org/pub/satcat.csv](http://celestrak.org/pub/satcat.csv)

#### 2. UCS Satellite Database

- **Source:** Union of Concerned Scientists
- **Use in this project:** higher-fidelity payload metadata including ownership, mission, launch mass, and lifetime fields
- **Link:** [http://www.ucsusa.org/resources/satellite-database](http://www.ucsusa.org/resources/satellite-database)

#### 3. ESA Space Environment Report 2025

- **Source:** ESA Space Debris Office
- **Use in this project:** external benchmark for assumptions, validation checks, and proxy reasoning
- **Link:** [https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf](https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf)

### Analytical Framing

The project combines data engineering, orbital mechanics, and query-driven analysis.

- **Temporal growth modeling:** separate the historical launch regime from the modern acceleration regime and test the proposed pivot around 2014
- **Physics-informed risk metrics:** use orbital geometry, velocity, and kinetic energy to move beyond simple object counts
- **Relational structure:** separate the master dataset into reusable SQLite tables so the main project questions can be answered with focused queries rather than repeated notebook-only transforms
- **Narrative emphasis:** connect launch growth, altitude crowding, and non-operational object persistence into a single collision-risk story

### Usage & Reproduction

This repository includes all output artifacts generated from a full pipeline refresh, ensuring that every query result, visualization, and analysis matches the state of the data at project completion. By tracking all outputs (including executed notebooks, query results, and visuals), reviewers can directly verify the narrative, figures, and conclusions without needing to rerun the pipeline or regenerate data.

**Why include all outputs?**  

- Guarantees that the presentation, analysis, and visuals are reproducible and match the documented story, regardless of future data or package changes.
- Enables reviewers to audit, review, or reuse the final results without running the full pipeline.
- Preserves the exact state of the project as submitted, including all intermediate and final data products.

**Quick review:**  
If you only want to review the final presentation and results, simply install the dependencies and open `notebooks/output/08_orbital_debris_assessment_presentation_executed.ipynb`. All supporting outputs and data are included for reference.

#### 1. Installation & Environment Setup

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

#### 2. Pipeline Execution

To fully reproduce or update the outputs, run the pipeline from the `notebooks/` directory using the CLI options below. This will regenerate all outputs, but is not required for review unless you wish to update or extend the analysis.

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

#### 3. Output & Documentation Review

- Review executed notebooks in `notebooks/output/` (look for `_executed.ipynb` files).
- For a summary, see `08_orbital_debris_assessment_presentation.ipynb`.
- To view documentation in Jupyter, use `00_markdown_viewer.ipynb`.

**Recommended Workflow:**  
This project is designed for reproducible, stepwise analysis—no manual notebook editing required. The recommended workflow is:

1. **Set up your environment** (one-time)
2. **Run the pipeline** with a single command
3. **Review outputs** in the output folder or use the markdown viewer for documentation

**Manual Execution:**  
You may run each notebook in order for full control (see notebook list above), but the CLI is recommended for reproducibility.

- Use the `execute.py` command to run the pipeline and generate outputs.
- Review results in the output folder, not the original notebooks.
- Use the markdown viewer notebook for in-notebook documentation access.
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

AI assistance (primarily GitHub Copilot) was utilized as a development tool for formula and function development, error debugging, and documentation adjustments. AI-assisted functions are explicitly identified in their respective headers.

**Human Authorship & Governance**  
I retain full authorship and responsibility for the following core components:

- **Strategic Framework:** Research direction, conceptual framing, and methodology.
- **Data Architecture:** All data-cleaning logic, schema definitions, and pipeline design.
- **Analytical Logic:** Query structure, data interpretation, and final conclusions.
- **Critical Judgment:** Final assumptions and technical tradeoff decisions.

**Verification & Accountability**  
All AI-generated suggestions underwent rigorous manual review, verification, and editing prior to usage in any way. I remain fully accountable for the accuracy, integrity, and logic of the completed work in its entirety.
