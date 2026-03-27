### IN PROGRESS
# Orbital Debris Assessment: Mapping the Kessler Acceleration in Low Earth Orbit

**Author:** James Glosser  
**Contact:** [Email](mailto:DemonicUrges05@gmail.com) | [LinkedIn profile](https://www.linkedin.com/in/james-glosser-249100204/)  
**Repository:** [GitHub repository](https://github.com/sithid/orbital-debris-assessment)  
**Last Updated:** March 2026  
**Status:** Code:You Capstone Project #4 (Data Analysis Pathway), updated to reflect the current notebook -> SQLite -> query -> visualization workflow.

---

## Project Overview

This capstone examines whether low Earth orbit is entering a more dangerous growth regime driven by rapid satellite deployment, persistent rocket bodies, and long-lived debris. The project started as a flat-file workflow centered on `kinetic_master.csv`, but the current structure is more deliberate: clean the source datasets, synthesize a physics-informed master registry, normalize that registry into SQLite, run focused analytical queries, and generate final visualizations from compact query outputs.

The goal is not just to count objects in orbit. It is to identify when orbital growth shifts from a historical linear pattern into a modern acceleration regime, and to map where the highest-risk objects are concentrating by orbit class, altitude band, and object type.

This README follows the project narrative laid out in [docs/Capstone Project Proposal - James Glosser.md](docs/Capstone%20Project%20Proposal%20-%20James%20Glosser.md), but updates it to match the repository's current flow and artifacts.

## Research Questions

### Primary Questions

- At what year did orbital growth decouple from a historical linear trend and transition into an exponential trajectory?
- How are high-risk objects, measured through velocity and kinetic energy, distributed across orbit classes and altitude bands, especially in the 400-600 km LEO band?
- Which ownership or operator groups contribute most to non-operational zombie payload concentrations?

### Secondary Questions

- How do launch cohorts and post-2014 deployment patterns affect congestion intensity?
- How do object type and operational status relate to kinetic risk?
- Do user categories such as commercial, government, military, and civil show distinct risk profiles?

## Current Workflow

The repo is organized as a staged analysis pipeline. Each notebook handles a distinct phase of the project.

1. **Pipeline Refresh**   
   `notebooks/00_pipeline_refresh.ipynb.ipynb` downloads original datasets from their respective sources.

2. **Analysis scratchpad**  
   `notebooks/00_analysis_scratchpad.ipynb` is the project's working notebook for raw notes, exploratory checks, math research, diagnostic snippets, and in-progress thinking.

3. **UCS cleanup**  
   `notebooks/01_ucs_cleanup.ipynb` standardizes and validates the UCS satellite registry, producing `data/clean/ucs_cleaned.csv`.

4. **SATCAT cleanup and reconstruction**  
   `notebooks/02_satcat_cleanup.ipynb` cleans the SATCAT catalog, repairs missing orbital values, and exports `data/clean/satcat_cleaned.csv`.

5. **Master synthesis**  
   `notebooks/03_kinetic_master_synthesis.ipynb` merges the cleaned sources into the physics-informed master dataset `data/clean/kinetic_master.csv`.

6. **SQLite normalization**  
   `notebooks/04_orbital_debris_synthesis.ipynb` converts the master dataset into a normalized SQLite database at `data/clean/orbital_debris.db`.

7. **Analytical query layer**  
   `notebooks/05_orbital_debris_queries.ipynb` runs project queries against the SQLite database and exports compact parquet result sets to `data/clean/queries/`.

8. **Visualization layer**  
   `notebooks/06_visualizations.ipynb` reads the query outputs and generates the final figures in `images/`.

## Repository Structure

```text
orbital-debris-assessment/
|- data/
|  |- original/              # raw source files
|  \- clean/                 # cleaned CSVs, SQLite database, parquet query outputs
|- docs/                     # capstone proposal and supporting documentation
|- images/                   # exported figures and schema image
|- notebooks/                # stepwise analysis pipeline
|- README.md
\- requirements.txt
```

## Key Data Products

| Artifact | Current Role | Size |
| --- | --- | --- |
| `data/clean/ucs_cleaned.csv` | Cleaned UCS satellite registry | 7,542 rows x 34 columns |
| `data/clean/satcat_cleaned.csv` | Cleaned SATCAT global catalog | 68,087 rows x 27 columns |
| `data/clean/kinetic_master.csv` | Physics-informed synthesized master dataset | 33,234 rows x 47 columns |
| `data/clean/orbital_debris.db` | Normalized SQLite analysis database | 6 relational tables |
| `data/clean/queries/pq1_launch_trend.parquet` | Query output for launch growth analysis | 69 rows x 6 columns |
| `data/clean/queries/pq2_high_risk.parquet` | Query output for high-risk distribution analysis | 18 rows x 12 columns |

The SQLite database currently contains these tables:

- `satellites`
- `orbital_data`
- `ucs_details`
- `risk_assessment`
- `ownership_operators`
- `launch_events`

## Data Sources

### 1. CelesTrak Satellite Catalog (SATCAT)

- **Source:** CelesTrak / U.S. Space Command (USSPACECOM)
- **Use in this project:** baseline global object catalog for payloads, rocket bodies, and debris
- **Link:** [http://celestrak.org/pub/satcat.csv](http://celestrak.org/pub/satcat.csv)

### 2. UCS Satellite Database

- **Source:** Union of Concerned Scientists
- **Use in this project:** higher-fidelity payload metadata including ownership, mission, launch mass, and lifetime fields
- **Link:** [http://www.ucsusa.org/resources/satellite-database](http://www.ucsusa.org/resources/satellite-database)

### 3. ESA Space Environment Report 2025

- **Source:** ESA Space Debris Office
- **Use in this project:** external benchmark for assumptions, validation checks, and proxy reasoning
- **Link:** [https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf](https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf)

## Analytical Framing

The project combines data engineering, orbital mechanics, and query-driven analysis.

- **Temporal growth modeling:** separate the historical launch regime from the modern acceleration regime and test the proposed pivot around 2014
- **Physics-informed risk metrics:** use orbital geometry, velocity, and kinetic energy to move beyond simple object counts
- **Relational structure:** separate the master dataset into reusable SQLite tables so the main project questions can be answered with focused queries rather than repeated notebook-only transforms
- **Narrative emphasis:** connect launch growth, altitude crowding, and non-operational object persistence into a single collision-risk story

## Current Outputs

The repo currently includes these exported visuals:

- `images/orbital_debris_schema_erd.png`
- `images/launch_trends_pq1.png`
- `images/launch_trends_pq1.svg`
- `images/high_risk_distribution_pq2.png`
- `images/high_risk_distribution_pq2.svg`

At the moment, the committed visualization layer is strongest for Primary Question 1 and Primary Question 2. The database and query structure are already in place to support the remaining analysis work.

## How To Reproduce

### 1. Installation

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

### 2. Run the notebooks in pipeline order

If you do not wish to run each notebook indivudually, in ordered sequence, you can run execute.py to do it for you.

```bash
# Run all notebooks in order. Download original datasets.
python execute.py --refresh

# Run all notebooks excluding 00_pipeline_refresh.  Do NOT download source datasets.
# Run this if you already ran the pipeline refresh / already have the original source documents and only
# want to rerun all notebooks after pipeline_refresh.
python execute.py
```

If you would prefer, you can also run each notebook in ordered sequence. If you already have the original dataset CSVs, you can skip `00_pipeline_refresh.ipynb`.

1. `notebooks/00_pipeline_refresh.ipynb`
2. `notebooks/01_ucs_cleanup.ipynb`
3. `notebooks/02_satcat_cleanup.ipynb`
4. `notebooks/03_kinetic_master_synthesis.ipynb`
5. `notebooks/04_orbital_debris_synthesis.ipynb`
6. `notebooks/05_orbital_debris_queries.ipynb`
7. `notebooks/06_visualizations.ipynb`

Optional notebooks:

- `notebooks/00_analysis_scratchpad.ipynb` for exploratory checks, working notes, and scratch analysis, etc.

If the cleaned data, SQLite database, and parquet query outputs already exist and you need to regenerate the charts, running `notebooks/06_visualizations.ipynb` is enough.

## Assumptions and Limitations

- SATCAT and UCS do not provide identical coverage, so matching quality depends on shared identifiers and metadata consistency.
- Some physics and mass fields require imputation or derivation rather than direct observation.
- The SQLite layer improves reproducibility, but it does not eliminate source-era gaps or historical catalog inconsistencies.
- High-risk summary tables can contain missing average values where a group exists but no object in that group qualifies as high risk.

## Why This Structure Matters

The old flat-file-centered workflow made it too easy to mix cleaning, modeling, querying, and storytelling in the same place. The current structure separates those concerns:

- cleaned source registries for repeatable preprocessing
- a master synthesis layer for feature engineering
- a normalized SQLite database for structured analysis
- query outputs that freeze the logic for each research question
- a visualization notebook that focuses only on presentation

## AI Usage & Authorship Note

AI assistance (primary GitHub Copilot) was utilized as a development tool for formula research, some functions, error debugging, and documentation adjustments.

**Human Authorship & Governance** I retain full authorship and responsibility for the following core components:

- **Strategic Framework:** Research direction, conceptual framing, and methodology.
- **Data Architecture:** All data-cleaning logic, schema definitions, and pipeline design.
- **Analytical Logic:** Query structure, data interpretation, and final conclusions.
- **Critical Judgment:** Final assumptions and technical tradeoff decisions.

**Verification & Accountability** All AI-generated suggestions underwent rigorous manual review, verification, and editing prior to implementation. AI-assisted functions are explicitly identified in their respective headers. I remain fully accountable for the accuracy, integrity, and logic of the completed work.
