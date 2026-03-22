**Capstone Project Proposal (Data Analysis Pathway)**

**Project Title:** Orbital Debris Assessment: Mapping the Kessler Acceleration in Low Earth Orbit

**Proposed By:** James Glosser

**GitHub Repository:** [https://github.com/sithid/orbital-debris-assessment](https://github.com/sithid/orbital-debris-assessment)

**Project Overview**

This project investigates how rapid satellite deployment, persistent rocket bodies, and long-lived debris are reshaping collision risk in low Earth orbit. I will convert my cleaned kinetic\_master.csv workflow into a normalized SQL database so the analysis is structured, reproducible, and query-driven rather than flat-file dependent. The central objective is to identify the decoupling point where orbital growth shifts from a historical linear pattern into an exponential trajectory, and to map the resulting risk hotspots by object type, altitude band, and operator profile.

## Data Sources

### 1. CelesTrak Satellite Catalog (SATCAT)

-   **Source:** CelesTrak / U.S. Space Command (USSPACECOM)
-   **Relevant fields:** norad\_id, cospar\_id, object\_name, object\_type, ops\_status, owner, owner\_code, launch\_date, launch\_site, decay\_date, period\_minutes, inclination\_degrees, apogee\_km, perigee\_km, rcs, data\_status\_code, orbit\_type
-   **Link**: [**http://celestrak.org/pub/satcat.csv**](http://celestrak.org/pub/satcat.csv)

### 2. UCS Satellite Database (UCS-Satellite-Database)

-   **Source:** Union of Concerned Scientists (UCS)
-   **Relevant fields:** norad\_id, cospar\_id, satellite\_name, official\_name, country\_operator, owner, users, purpose, detailed\_purpose, orbit\_class, orbit\_type, geo\_longitude, perigee\_km, apogee\_km, eccentricity, inclination\_degrees, period\_minutes, launch\_mass\_kg, dry\_mass\_kg, power\_watts, launch\_date, lifetime\_years, contractor, contractor\_country, launch\_site, launch\_vehicle, un\_registry
-   **Link:** [**http://www.ucsusa.org/resources/satellite-database**](http://www.ucsusa.org/resources/satellite-database)

### 3. Optional/Reference: ESA Space Environment Report 2025

-   **Source:** ESA Space Debris Office
-   **Use:** benchmarking and proxy assumptions for mass/composition
-   **Link:** [**https://www.sdo.esoc.esa.int/publications/Space\_Environment\_Report\_I9R1\_20251021.pdf**](https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf)

## Research Objectives

### Primary Questions

-   At what year did orbital growth decouple from a historical linear trend and transition into an exponential trajectory?
-   How are high-risk objects (by velocity and kinetic energy) distributed across orbit classes and altitude bands, especially in the 400 - 600 km LEO?
-   Which ownership/operator groups contribute most to non-operational “zombie” payload concentrations?

### Secondary/Exploratory Questions

-   How do launch cohorts and post-2014 deployment patterns affect congestion intensity?
-   How do object type (PAYLOAD, ROCKET BODY, DEBRIS) and operational status relate to kinetic risk?
-   Do user categories (commercial, government, military, civil) show distinct risk profiles?

These objectives are valuable because they combine temporal growth modeling (figuring out exactly when space got too crowded, the decoupling point) with physics-based risk segmentation (grouping the junk by how deadly it is, not just counting it), producing findings that are both mathematically solid and easy enough to understand.

## Data Preparation Approach

-   Standardize schemas and datatypes across SATCAT and UCS extracts.
-   Align datasets primarily on norad\_id, with cospar\_id and launch metadata available for validation checks.
-   Handle missing values with documented tiering: measured values first, derivations second, statistical proxies third.
-   Flag implausible outliers (e.g., invalid orbital geometry or non-physical values like negative mass, negative period, etc) and apply bounded treatment (don’t just blindly delete things) only when needed for visualization stability.
-   Engineer derived fields: sat\_age\_years, velocity\_kms, kinetic\_joules, in\_orbit, is\_zombie, risk bands.
-   Implement relational SQL structure with linked tables from different sources, including: satellites, orbital\_data, ownership\_operators, launch\_events, ucs\_details, risk\_assessment, joined by norad\_id, owner\_code, and launch\_id.
-   Datasets cleaned and combined into a final dataset, kinetic\_master, which standardizes various columns between the two (OBJECT\_ID from SATCAT which is the cospar/international designator and ‘COSPAR Number’ from UCS, both standardized to cospar\_id in the final kinetic\_master csv, etc).

## Current Status

-   SATCAT and UCS raw data acquired, inspected, and cleaned in notebook-based stages.
-   kinetic\_master.csv created with integrated physics, ownership, and risk attributes.
-   DBML schema drafted and relationship mapping established.
-   Prior analysis already identified a provisional decoupling/pivot period around 2014, to be revalidated via SQL-backed workflow.

## Deliverables (Remaining Work)

### Required Tasks (must be completed)

-   Finalize SQL schema and constraints from DBML.
-   Build SQLite database and load normalized tables.
-   Create reproducible ETL/load scripts (csv to sql).
-   Implement analysis queries/functions for all primary questions, including decoupling-point detection.
-   Produce required visualizations (growth model pivot, altitude-risk distribution, ownership/zombie analysis).
-   Update README, data dictionary, and methodology notes.
-   Perform data integrity checks (keys, row counts, null audits, join validation).

## Project Timeline

-   Phase 1: Finalize schema, create SQLite database, load core tables.
-   Phase 2: Complete ETL automation, run validation checks, and baseline exploratory SQL.
-   Phase 3: Run core analyses and decoupling-point model; generate required charts and interpretation notes.
-   Phase 4: Refine findings, polish repository artifacts, finalize deliverables and presentation ( ~15min presentation for code:you interviewer ).

## Additional Considerations

-   Assumptions: many mass/power values for non-UCS objects are imputed rather than directly measured.
-   Limitations: identifier inconsistencies and historical completeness vary by source and era.
-   Risks: The main risks are changing table definitions over time, imperfect record matching between datasets, and slower query performance as join complexity grows.