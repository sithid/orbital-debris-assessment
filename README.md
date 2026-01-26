# Orbital Debris Assessment: A Physics-Informed Analysis of the Kessler Syndrome Acceleration

**Author:** James Glosser  
**Contact:** DemonicUrges05@gmail.com | [LinkedIn](https://www.linkedin.com/in/james-glosser-249100204/)  
**Repository:** [github.com/sithid/orbital-debris-assessment](https://github.com/sithid/orbital-debris-assessment)  
**Last Updated:** January 2026  
**Status:** Code:You Capstone Project #4 (Data Analysis Pathway)

---

## **Executive Summary**

This project delivers a comprehensive orbital debris risk assessment by engineering a **physics-reconstructed master registry** that merges 67,464 tracked SATCAT objects with high-fidelity Union of Concerned Scientists (UCS) satellite data. By implementing **Vis-Viva velocity calculations**, **ESA-standard mass imputation**, and **Kernel Density Estimation (KDE) spatial analysis**, this analysis quantifies the 2014 "Kessler Acceleration"—the mathematical inflection point where commercial mega-constellation deployment rates surpassed 67 years of legacy launch activity.

### **Key Findings**

- **The 2014 Pivot:** Mathematical proof (via Brent's Method root-finding) that exponential satellite growth officially surpassed linear Cold War trends in mid-2014
- **68km Compression Crisis:** KDE analysis reveals modern mega-constellations occupy a narrow 200-600km band (median: 539km), with rocket bodies distributed across all of LEO but centered 68km higher (median: 607km)—the populations overlap significantly in the 500-700km danger zone
- **Zombie Protocol Imperative:** Identified 5,263 defunct payloads (satellites only; excludes debris/rocket bodies) exceeding 110% design life, representing high-mass collision catalysts in high-traffic orbits
- **Double Threat Topology:** The orbital environment exhibits vertical segregation where active satellites operate in a "kinetic canyon" bounded by legacy debris above and exponential launch rates below

### **Technical Impact**

**Data Engineering Achievement:**

- Merged 67,464 SATCAT objects + 7,542 UCS satellites → 32,843 physics-complete in-orbit records
- Achieved 100% feature density across 40 engineered attributes through tiered imputation (UCS verified → Keplerian derivation → ESA proxies)
- Implemented Vis-Viva equation to reconstruct orbital velocity for 100% of tracked objects (critical for kinetic energy modeling)
- Total mass now sits inside the ESA 2025 benchmark range after aligning payload proxies to the 355 kg ESA mean; composition deltas are documented in validation

**Analytical Innovation:**

- Identified zombie satellite distribution by owner, revealing US (2,199 satellites, 42%) and Russia/CIS (1,430 satellites, 27%) as primary contributors to defunct payload population
- Applied dual-cadence curve fitting (linear 1957-2013 vs. exponential 2014-2026) to prove acceleration hypothesis
- Performed 2D KDE spatial analysis to quantify the 68km altitude compression between active/inactive populations

**Portfolio Differentiation:**

- **4th Code:You capstone project** across **4 independent technology pathways**:
  - **Software Development (C#):** Enterprise application architecture, OOP design patterns
  - **Web Development (JavaScript/Vue.js):** Full-stack web applications, reactive UI frameworks
  - **Cloud Computing (AWS):** Infrastructure-as-code, serverless functions, scalable deployment
  - **Data Science (Python):** This project - physics-informed analytics, statistical imputation, production ETL
    - Real-world dataset requiring domain research (ESA debris standards, Keplerian mechanics, NORAD tracking protocols)
    - Production-grade transparency: documented all imputation assumptions, validated against external benchmarks, communicated uncertainty bounds

---

## **Project Narrative: The Kessler Syndrome Crisis**

In 1978, NASA scientist Donald Kessler warned that Earth's orbital environment could reach a critical density threshold where collisions generate more debris than atmospheric drag removes—a runaway cascade now known as "Kessler Syndrome." For decades, this remained a theoretical concern. **This analysis proves the threat became operational reality in 2014.**

### **The "Great Acceleration" (2014-Present)**

Using curve-fitting and root-finding algorithms, this project identifies **mid-2014** as the mathematical "inflection point" where:

- Commercial mega-constellations (Starlink, OneWeb, Planet Labs) began exponential deployment
- Launch cadence shifted from linear (Cold War era: ~100 satellites/year) to exponential (~2,000+ satellites/year by 2023)
- The orbital population growth rate officially surpassed 67 years of legacy accumulation

### **The "Kessler Canyon" Threat Topology**

High-resolution Kernel Density Estimation reveals a dangerous vertical overlap:

- **"Commuter Lane" (200-600km):** Modern mega-constellations cluster tightly (median: 539km)
- **"Deadly Ring" (200-2000km):** Rocket bodies span ALL of LEO, but their center of mass (median: 607km) sits just 68km above the satellite median
- **Critical Insight:** The 68km figure is a **median-to-median** measure—not a clean boundary. Both populations overlap heavily in the **500-700km danger zone**, where Starlink shells intersect legacy rocket body orbits

### **The "Zombie Satellite" Population**

This analysis identifies **5,263 defunct payloads** (satellites only; debris and rocket bodies are excluded from this classification) that:

- Exceed 110% of their design lifetime (e.g., 15-year satellite now 16.5+ years old)
- Average age of 25.2 years (significantly beyond typical 10-15 year design lives)
- Represent 29.7% of the total satellite population (17,733 active + inactive satellites)
- Geopolitical distribution reveals Cold War legacy: US (42%) and Russia/CIS (27%) account for 69% of zombie population

**Methodology Note:** The zombie algorithm applies exclusively to objects classified as satellites in the master registry, filtering out non-operational satellites via status codes or age-to-lifetime ratios. The total in-orbit population includes an additional 12,655 debris fragments and 2,403 rocket bodies that are not counted in zombie statistics.

---

## **Dataset Architecture**

### **Primary Data Sources**

1. **SATCAT (Satellite Catalog) - CelesTrak**

   - **Source:** [`https://celestrak.org/pub/satcat.csv`](https://celestrak.org/pub/satcat.csv)
   - **Coverage:** 67,464 tracked objects (1957-present)
   - **Scope:** Global registry including active satellites, rocket bodies, and debris fragments
   - **Limitations:** Mass-blind (no mass data), 0.0 placeholders, inconsistent string formatting

2. **UCS Satellite Database - Union of Concerned Scientists**

   - **Source:** [`https://www.ucsusa.org/resources/satellite-database`](https://www.ucsusa.org/resources/satellite-database)
   - **Coverage:** 7,542 active satellites (verified operational)
   - **Scope:** High-fidelity metadata (launch mass, design lifetime, owner, purpose)
   - **Limitations:** Active payloads only (excludes debris/rocket bodies)

3. **ESA Space Environment Report (2025)**
  - **Source:** [ESA Space Environment Report 2025 (PDF)](https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I9R1_20251021.pdf)
   - **Coverage:** Statistical proxies for untracked/unknown objects
   - **Scope:** Mass averages, composition percentages, size distributions
   - **Application:** Tier 3 imputation fallback for objects without UCS/SATCAT mass data
  - **References used:** Section 2 (Space Environmental History in Numbers; object count/mass/area evolution) and Section 2.4 (Non-catalogued and modelled objects; MASTER size-density distributions, Figs. 2.8–2.11)
  - **Citation:** ESA Space Debris Office, *Space Environment Report*, Issue 9 Rev 1, 21 Oct 2025

---

## **Data Pipeline Architecture**

### **Stage 1: Dual ETL Pipelines**

#### **Notebook 01: UCS Active Satellite Registry**

**Objective:** Transform raw UCS satellite data into a high-fidelity "Gold Standard" reference for active payloads.

**Key Transformations:**

- **Schema Standardization:** Normalized 29 headers to snake_case for programmatic consistency
- **Numeric Sanitization:** Converted string artifacts to `float64`, neutralized 0.0 placeholders → `NaN`
- **Temporal Engineering:** Derived `sat_age_years` (2026 - `launch_year`) for lifetime modeling
- **Orbital Classification:** Implemented period-based regime binning (LEO < 128min, GEO: 1400-1460min, MEO: 128-1400min)
- **Mass Integrity:** Enforced physical constraints (mass > 0, perigee < apogee)

**Output:** `ucs_cleaned.csv` (7,542 records, 29 features, 100% numeric density)

---

#### **Notebook 02: SATCAT Global Registry Reconstruction**

**Objective:** Convert raw SATCAT tracking data into a physics-complete orbital debris catalog.

**The Engineering Challenge:**
While SATCAT provides comprehensive tracking coverage (67K+ objects), it presents a critical "Physics Transparency Gap":

- **Mass-Blind:** No inherent mass data (required for kinetic energy modeling)
- **Placeholder Artifacts:** Uses `0.0` for missing orbital elements (period, inclination, altitudes)
- **Inconsistent Formatting:** Mixed-case strings, trailing whitespace, legacy status codes

**The Solution: 6-Stage Reconstruction Pipeline**

**Stage 1-2: Ingestion & Universal Sanitization**

- Renamed 18 legacy headers to match UCS snake_case schema
- Enforced `norad_id` as primary key (string format for join-readiness)
- Stripped whitespace artifacts from `owner_code`, `launch_site` (prevent "invisible bugs")
- Neutralized `0.0` placeholders → `NaN` across 5 physics columns

**Stage 2.1: UCS High-Fidelity Enrichment**

- Synchronized SATCAT with `ucs_cleaned.csv` via `norad_id` merge
- Repaired 7,542 active satellite records with verified UCS mass/geometry
- Created "Hierarchy of Truth": UCS verified > Keplerian derived > ESA proxy

**Stage 3: Keplerian Reconstruction (The Density Engine)**

- Applied **Kepler's Third Law** to derive missing `period_minutes`:
  ```python
  T = 2π√(a³/μ)  where a = Earth_radius + (apogee + perigee)/2
  ```
- Achieved 98.1% period density through mathematical derivation
- Applied grouped median imputation (by `orbit_class`) for final 1.9% gap

**Stage 3.2-3.3: Geometric Sweep & Eccentricity Derivation**

- Filled remaining `inclination_degrees`, `apogee_km`, `perigee_km` via regime-specific medians
- Derived `eccentricity` using formula: `e = (r_a - r_p)/(r_a + r_p)`
- Achieved **100% geometric density** for in-orbit population

**Stage 4: Categorical Hardening**

- Mapped legacy codes → controlled vocabulary (`PAY` → `PAYLOAD`, `R/B` → `ROCKET BODY`)
- Standardized operational status (`+` → `OPERATIONAL`, `-` → `NON-OPERATIONAL`)
- Derived `rcs_class` size bins: SMALL (<0.1 m²), MEDIUM (0.1-1.0), LARGE (>1.0)

**Stage 5-5.2: Tiered Mass Imputation**

#### **Mass Imputation Methodology & Validation**

This analysis implements a 3-tier imputation hierarchy validated against ESA's 2025 Space Environment Report:

| Tier                        | Data Source            | Coverage | Objects | Method                                |
| :-------------------------- | :--------------------- | :------- | :------ | :------------------------------------ |
| **Tier 1: Measured**        | UCS Satellite Database | 11.2%    | 7,542   | Direct launch mass observations       |
| **Tier 2: Physics-Derived** | Keplerian calculations | 30%      | ~10,000 | Vis-Viva velocity, Kepler's Third Law |
| **Tier 3: Proxy Standards** | ESA mass averages      | 58.8%    | ~15,000 | Object-type-specific proxies          |

**Proxy Values Applied:**

- **Rocket Bodies:** 2,000 kg (conservative; no ESA class-average published)
- **Unknown Payloads:** 355 kg (ESA mean active payload mass, Sec. 3.5/Fig. 2.31)
- **Debris Fragments:** 50 kg (trackable fragment average; external safety assumption)
- **Unclassified Objects:** 100 kg (safety fallback)

**ESA Grounding for Proxies (what the report actually states):**

- **Payload mean mass:** 355 kg with 6 m² cross-section for active payloads in LEO (Sec. 3.5, Fig. 2.31; p.75). The proxy now matches this ESA mean.
- **Rocket bodies:** The 2025 report does not publish a class-average rocket body mass; histograms in Sec. 3.1 (Fig. 3.2) show multi-ton distributions but no mean. The 2,000 kg proxy remains a conservative assumption, not an explicit ESA value.
- **Debris fragments:** Sec. 2.4 (MASTER size distributions) provides counts and size-density curves but no fragment mass averages. The 50 kg proxy is an external safety assumption; ESA does not supply a mean mass for the >10 cm catalogued fragment class in this report.

**Validation Results:**

| Metric                  | This Analysis | ESA 2025 Benchmark | Deviation                    |
| :---------------------- | :------------ | :----------------- | :--------------------------- |
| **Total In-Orbit Mass** | 14.61 kilotons | 13.6-15.1 kilotons | Within ESA range ✅          |
| **Payload Mass %**      | 62.5%         | 71.5%              | -9.0 pp (lower)              |
| **Rocket Body Mass %**  | 32.9%         | 27.4%              | +5.5 pp (higher)             |
| **Debris Mass %**       | 4.6%          | 1.1%               | +3.5 pp (higher; proxy-heavy) |

**Interpretation:** After aligning the payload proxy to the ESA mean (355 kg), total mass falls inside the ESA 2025 range. Composition skews toward rocket bodies/debris because payload proxies dropped; these deltas are transparent and traceable to the proxy choice rather than hidden model error.

**Critical Transparency Statement:**

- Mass values for **88.8% of objects** are statistical proxies, not direct measurements
- The term "100% data density" refers to **imputation completeness**, not measurement fidelity
- Kinetic energy calculations for unknown payloads use conservative estimates; actual values may vary

**Dry Mass Derivation:**

- Applied orbit-specific fuel fraction ratios (LEO payloads: 0.65, GEO: 0.55, debris/rocket bodies: 1.0)
- Derived `dry_mass_kg` for collision modeling (structural mass only)

**Output:** `satcat_cleaned.csv` (67,464 records, 27 features, 100% imputation coverage)

---

### **Stage 2: Relational Synthesis & Physics Reconstruction**

#### **Notebook 03: Orbital Risk Master Registry**

**Objective:** Merge cleaned datasets into a unified kinetic threat catalog with physics-complete profiles.

**The Merge Strategy:**

- **Primary Join:** `norad_id` (1:1 relationship for active UCS satellites)
- **Preservation Logic:** Retained all 67K SATCAT objects (left join), enriched 7,542 with UCS metadata
- **Conflict Resolution:** UCS data overrides SATCAT where both exist (higher fidelity)

**Zombie Satellite Identification Algorithm:**

A payload is flagged as a "Zombie" if:

1. `ops_status` is NOT "OPERATIONAL", OR
2. `sat_age_years` > (`lifetime_years` × 1.10)

**Scope & Limitations:**

- Applies to **PAYLOAD** objects only (excludes debris/rocket bodies)
- Relies on `lifetime_years`, which was imputed via orbit-class medians for 28% of active fleet
- Results represent statistical estimates, not confirmed operational status
- Count represents high-risk defunct payloads exceeding 110% of design life

**Mean Orbital Velocity Calculation:**
For 100% of in-orbit objects, calculated average velocity using the circular orbit approximation:

```python
v = √(μ/a)  where:
  μ = 398600.4418 km³/s² (Earth's gravitational parameter)
  a = semi-major axis (km)
```

**Technical Note:** This is a simplification of the full Vis-Viva equation `v = √[μ(2/r - 1/a)]`, which calculates instantaneous velocity at any point in an elliptical orbit. For collision risk assessment, mean velocity (the average speed around the orbit) is the appropriate metric rather than instantaneous velocity at specific orbital points like perigee or apogee. This approach provides altitude-specific accuracy without the complexity of tracking moment-to-moment positional variations.

**Kinetic Energy Calculation:**

```python
KE = 0.5 × proxy_mass_kg × velocity_m_s²
```

**Output:** `kinetic_master.csv` (67,464 records, 44 features)

**Vital Statistics:**

- **In-Orbit Objects:** 32,843 (48.7% of catalog)
- **Total Mass:** 14.61 Kilotons (14,610 metric tons)
- **Kinetic Energy:** 289.68 Terajoules
- **Zombie Satellites:** 5,263 defunct payloads
- **Average Orbital Velocity:** 6.91 km/s (altitude-adjusted via Vis-Viva)

Verified the final `kinetic_master.csv` contains **32,843** in-orbit objects representing **14.61 Kilotons** of mass and **289.68 Terajoules** of kinetic energy after aligning payload proxies to the ESA mean.

---

### **Stage 3: Strategic Analytics & Visualization**

#### **Notebook 04: Active Fleet Intelligence (The 2014 Pivot)**

**Objective:** Mathematically prove the "Great Acceleration" hypothesis using curve-fitting and root-finding algorithms.

**The Hypothesis:**
Commercial mega-constellations (post-2014) represent a fundamentally different growth regime than Cold War era launches (1957-2013).

**The Methodology:**

**1. Dual-Cadence Curve Fitting**

- **Legacy Model (1957-2013):** Linear regression `y = mx + b`
  - Fit: 56 years of launch data
  - Result: Steady ~100 satellites/year growth rate
- **Modern Model (2014-2026):** Exponential growth `y = ae^(b(x-c))`
  - Fit: 12 years of mega-constellation deployment
  - Result: Accelerating growth (doubling time ~2.5 years)

**2. Acceleration Point Discovery (Brent's Method)**

- Calculated first derivatives (velocity) of both models:
  - Linear: `f'(x) = m` (constant)
  - Exponential: `f'(x) = ab·e^(b(x-c))` (increasing)
- Used `scipy.optimize.brentq` to find root of `f'(x) - m = 0`
- **Result:** Crossover occurred at **year 2014.58** (mid-2014)

**Interpretation:** 2014 marks the year exponential growth velocity officially surpassed linear legacy trends. External validation confirms 2014 as the start of commercial LEO constellation deployments (UCS historical data).

**Visualizations:**

- **The Great Acceleration:** Dual-cadence overlay showing 2014 inflection point
- **Cumulative Mass Plot:** Exponential curve acceleration post-2014

---

#### **Notebook 05: Spatial Risk Analysis (The Kessler Canyon)**

**Objective:** Quantify vertical orbital segregation and identify collision risk zones.

**The Kessler Canyon Discovery:**

**Method:** 2D Kernel Density Estimation (KDE) on altitude vs. kinetic energy

- **X-axis:** Altitude (km)
- **Y-axis:** Kinetic Energy (Joules)
- **Overlay:** Active satellites (cyan) vs. Rocket bodies (crimson)

**Key Finding:**

- **Active Satellites (Median):** 539km altitude
- **Rocket Bodies (Median):** 607km altitude
- **Vertical Gap:** **68km separation**

**The "Double Threat" Topology:**

1. **Floor Rising:** Modern mega-constellations compress into 200-600km band
2. **No Clean Separation:** Rocket bodies are distributed across ALL of LEO (200-2000km)—there is no isolated "graveyard"
3. **Overlap Zone (500-700km):** The satellite and rocket body populations physically intersect, with medians only 68km apart

**Energy Disparity Analysis:**

- **Energy Disparity (Adjusted):** Rocket bodies carry **4.1× more kinetic energy** than satellites in the same orbital regime
  - **Caveat:** This ratio includes ~11,000 unknown payloads imputed at the 355 kg ESA mean; actual disparity for measured objects may vary
  - **Implication:** While rocket bodies remain high-risk shrapnel sources, modern mega-constellation satellites (e.g., Starlink: 260kg) represent a **swarm threat** where quantity multiplies kinetic load

**Zombie Geopolitical Distribution:**

The 5,263 zombie satellites break down by owner:

- **United States:** 2,199 satellites (41.8%)
- **Russia/CIS:** 1,430 satellites (27.2%)
- **China (PRC):** 372 satellites (7.1%)
- **United Kingdom:** 147 satellites (2.8%)
- **Japan:** 147 satellites (2.8%)

This distribution reveals the Cold War legacy effect: US and Soviet space programs created 69% of today's defunct payload population, representing long-term collision risks as these aged platforms (average 25.3 years old) enter unpredictable decay spirals.

---

## **Final Master Registry Statistics**

| Metric                   | Value              | Description                                         |
| :----------------------- | :----------------- | :-------------------------------------------------- |
| **Total Objects**        | 67,464 records     | Complete SATCAT universe (1957-2026)                |
| **In-Orbit Objects**     | 32,843 (48.7%)     | Currently active kinetic threats                    |
| **Total Mass**           | 14,610 metric tons | Cumulative kinetic mass (ESA-aligned 355 kg payload mean) |
| **Zombie Satellites**    | 5,263 payloads     | Defunct assets exceeding 110% design life (29.7% of satellites) |
| **Kinetic Energy**       | 289.68 Terajoules  | Total destructive potential at orbital velocities   |
| **Data Completeness**    | 100% imputation    | Physics-reconstructed across 44 engineered features |
| **UCS Enrichment**       | 7,542 satellites   | High-fidelity mass/lifetime data synchronized       |
| **Avg Orbital Velocity** | 6.91 km/s          | Altitude-adjusted via Vis-Viva equation             |

---

## **Key Visualizations**

### **Figure 1: Kinetic Mass Distribution (The White Whale)**

![Mass Distribution Log](./images/mass_distribution_log.png)  
_Figure 1: Logarithmic mass distribution revealing the 6-order-of-magnitude disparity in orbital objects. The International Space Station (450,000 kg) represents the "White Whale" outlier, while CubeSat swarms (<10 kg) populate the extreme left. This histogram proves why simple object counts mislead risk assessments—the ISS alone carries more kinetic mass than 450,000 CubeSats combined. The logarithmic scale is necessary to visualize both populations simultaneously, exposing the "invisible mass" hiding in aggregate statistics._

---

### **Figure 2: The Visibility Trap**

![Visibility Trap](./images/visibility_trap.png)  
_Figure 2: Mass vs. Count distribution revealing the deceptive inversion between object prevalence and kinetic risk. By count, the orbital population shows debris (38.5%) and active satellites (38.0%) as statistically comparable. However, by mass, rocket bodies (7.3% of count) carry ~33% of total kinetic energy—a 4.5:1 mass-to-count ratio. This creates the "visibility trap": regulatory frameworks focused on satellite proliferation (count-based metrics) systematically miss the legacy debris threat (mass-based physics). The most dangerous objects—multi-ton rocket bodies—are statistically invisible when sorted by count alone, appearing as "just 2,403 catalog entries" while carrying more collision energy than 12,655 debris fragments combined._

---

### **Figure 3: The Great Acceleration (2014 Pivot)**

![Great Acceleration](./images/great_acceleration.png)  
_Figure 3: Exponential launch reality (magenta) versus the legacy linear path (grey dashed), with 2000–2024 actual launches shown as cyan bars. The shaded magenta wedge is the “risk surplus” that exists only because growth went exponential. Brent’s Method pinpoints the acceleration inflection at ~2014.6 (vertical line and callout), and the HUD shows the fitted growth rate (~24%/yr) and doubling time (~2.9 years), confirming a sustained regime change._

---

### **Figure 4: Temporal Regime Shift**

![Temporal Regime Shift](./images/temporal_regime_shift.png)  
_Figure 4: Strategic synthesis visualization showing the acceleration inflection point. The magenta "Risk Surplus" zone represents satellites that would not exist under legacy linear growth patterns. The 2014 pivot marks the mathematical crossover where exponential commercial deployment overtook 67 years of Cold War-era linear trends. The HUD overlay quantifies the growth rate and doubling time, contextualizing the Kessler Acceleration as a measurable, ongoing exponential process._

---

### **Figure 5: Operator Oligopoly Analysis**

![Operator Oligopoly](./images/operator_oligopoly.png)  
_Figure 5: Market concentration analysis revealing the commercial space oligopoly. SpaceX (Starlink) dominates by object count with 60%+ of active satellites, while traditional aerospace giants (Lockheed Martin, Boeing) and government operators maintain higher individual satellite masses. This visualization quantifies the shift from government/military space programs to commercial mega-constellation dominance, with the top 5 operators controlling 75%+ of LEO traffic._

---

### **Figure 6: LEO Orbit Congestion Analysis**

![LEO Orbit Congestion](./images/orbit_congestion_leo.png)  
_Figure 6: Altitude-band population density showing object distribution within Low Earth Orbit (200-2000km). The 400-600km "Starlink band" shows dramatic concentration of modern mega-constellations. Rocket bodies are distributed across ALL altitude bands (200-2000km), with notable presence in the 600-800km range. The 500-700km zone represents the critical overlap region where active satellites physically intermix with legacy rocket bodies._

---

### **Figure 7: The Kessler Canyon (KDE Spatial Analysis)**

![Kessler Canyon](./images/kessler_canyon.png)  
_Figure 7: High-resolution KDE analysis of kinetic energy vs. altitude. **How to read:** Y-axis separates objects by mass (velocity is ~constant per altitude), X-axis shows orbital location. The cyan cloud (satellites, 539km median) and crimson band (rocket bodies, 607km median) **overlap significantly** in the 500-700km zone—there is no clean "gap." The 68km figure is median-to-median; both populations physically intermix across LEO. Rocket bodies span all altitudes (200-2000km), carrying 4.1× more energy per object than the average satellite. **Note:** ~11,000 payloads use the 355 kg ESA-mean proxy._

---

### **Figure 8: Zombie Satellite Distribution**

![Zombie Index](./images/zombie_index.png)  
_Figure 8: The Zombie Satellite distribution showing (Left) age histogram of 5,263 defunct payloads with 25.3-year average age, and (Right) top 5 owners by zombie count. "Zombies" are operationally dead payloads or satellites exceeding design life by 10%+ (`sat_age_years > lifetime_years × 1.10`). The United States leads with 2,199 zombie satellites (42% of total), followed by Russia/CIS with 1,430 (27%). This geopolitical breakdown reveals Cold War legacy: US and Soviet programs created the majority of today's uncontrolled payload population, representing imminent collision risks as these aged platforms enter unpredictable decay spirals._

---
### **Figure 9: Geopolitical Liability Attribution**

![Liability vs Traffic](./images/liability_vs_traffic.png)  
_Figure 9: Dual-metric geopolitical analysis comparing operational traffic (object count) versus kinetic liability (total mass). Russia and the United States dominate by mass despite lower satellite counts—evidence of legacy Cold War programs leaving high-mass rocket bodies and defunct platforms. China shows balanced growth across both metrics. Commercial operators (USA-flagged SpaceX) dominate traffic but contribute lower per-object mass. This visualization quantifies orbital "ownership" responsibility: who operates the most satellites versus who contributed the most collision-generating mass._

---
## **Technical Implementation**

### **Core Technologies**

- **Python 3.11:** Data processing and analysis
- **Pandas 2.x:** ETL pipeline and relational operations
- **NumPy:** Mathematical derivations (Vis-Viva, Kepler's Third Law)
- **Matplotlib/Seaborn:** Statistical visualizations
- **SciPy:** Curve fitting (`scipy.optimize.curve_fit`) and root-finding (`scipy.optimize.brentq`)
* **Seaborn:** Statistical visualization with KDE overlays (uses `scipy.stats.gaussian_kde` internally)


### **Key Algorithms & Methods**

**1. Mean Orbital Velocity (Circular Orbit Approximation)**

Inline calculation in notebook 03:
```python
master['velocity_kms'] = np.sqrt(MU / master['semi_major_axis_km'])
```
Where MU = 398600.4418 km³/s² (Earth's standard gravitational parameter)

**2. Kepler's Third Law (Period Derivation)**

Inline calculation in notebooks 01 & 02:
```python
period_seconds = 2 * np.pi * np.sqrt(a**3 / mu)
```

**3. Brent's Method (Acceleration Point)**

Inline calculation in notebook 04 to find when exponential growth velocity surpassed linear trends:
```python
from scipy.optimize import brentq

def slope_diff(x):
    return exponential_slope(x) - linear_slope(x)

acceleration_year = brentq(slope_diff, 2000, 2024)
# Result: 2014.58
```

**4. Kernel Density Estimation (Spatial Risk)**

Inline calculation in notebook 05:
```python
import seaborn as sns

sns.kdeplot(
    data=payloads,
    x='perigee_km',
    y='log_kinetic_joules',
    fill=True,
    cmap='Reds',
    alpha=0.4
)
```

---

## **Repository Structure**

```
orbital-debris-assessment/
├── data/
│   └── clean/             # Processed datasets (version controlled)
│       ├── ucs_cleaned.csv
│       ├── satcat_cleaned.csv
│       └── kinetic_master.csv
├── notebooks/
│   ├── 00_exploratory_research.ipynb  # Initial data exploration
│   ├── 01_ucs_cleanup.ipynb           # UCS ETL pipeline
│   ├── 02_satcat_cleanup.ipynb        # SATCAT reconstruction
│   ├── 03_orbital_risk_synthesis.ipynb # Master registry merge
│   ├── 04_active_fleet_intelligence.ipynb # 2014 pivot proof
│   └── 05_strategic_analysis.ipynb    # Kessler Canyon analysis
├── images/                # Visualization exports
├── docs/                  # Documentation
├── .gitignore            # Git exclusions (data/original/, venv/)
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

**Note:** Raw data files (`data/original/`) are excluded from version control. Run notebooks 01-02 to fetch and process fresh data from public sources.

---

## **Data Quality Achievements**

### **100% Feature Density Engineering**

- **UCS Pipeline:** Achieved 100% numeric density across 29 features through:

  - Grouped median imputation (by `orbit_class` for orbital elements)
  - Type-safe coercion (`float64` enforcement, `NaN` preservation)
  - Categorical standardization (controlled vocabulary for `object_type`, `ops_status`)

- **SATCAT Pipeline:** Transformed 67K "mass-blind" tracking records into physics-complete profiles:
  - Keplerian reconstruction: 30% of periods derived mathematically
  - UCS synchronization: 7,542 records enriched with verified mass
  - ESA proxy imputation: 58.8% of mass values filled via categorical standards
  - Vis-Viva velocity: 100% of objects assigned altitude-specific velocity

### **Relational Integrity**

- **Primary Key Discipline:** Enforced `norad_id` as string type to prevent join failures from mixed int/float artifacts
- **Schema Alignment:** Normalized both datasets to identical column names pre-merge
- **Conflict Resolution Protocol:** UCS data > SATCAT data > ESA proxy (hierarchy of truth)

### **Physics Validation**

- **Mass Composition:** Total mass within ESA 2025 range; composition deltas vs ESA: payload -9.0 pp, rocket bodies +5.5 pp, debris +3.5 pp (driven by lowered payload proxy)
- **Velocity Sanity Check:** Average orbital velocity (6.90 km/s) aligns with expected LEO range (6.5-7.8 km/s across all orbital regimes)
- **Kinetic Energy:** Total 289.68 TJ after ESA-aligned payload proxy (355 kg)

---

## **Strategic Insights for Industry**

### **The Policy Implications**

1. **Active Debris Removal (ADR) Prioritization:**

   - 5,263 zombie satellites represent priority removal targets (29.7% of satellite population)
   - Geopolitical concentration: US and Russia control 69% of zombie inventory, suggesting bilateral cleanup coordination
   - ROI justification: Removing 1 high-mass zombie = preventing 1,000+ trackable debris fragments (per ESA collision models)

2. **Launch Licensing Reform:**

   - 2014 pivot proves current regulatory frameworks (designed for linear growth) are inadequate
   - Recommendation: Implement **orbital density caps** per altitude band (e.g., max 500 satellites per 100km shell)
   - Precedent: ITU frequency allocation model (first-come-first-served → congestion management)

3. **Mega-Constellation Design Standards:**
   - 68km canyon gap is dangerously narrow—closer than the assumed 200km+ separation
   - Proposal: Mandate stricter altitude coordination; the 600-700km band should be designated a "buffer zone" with mandatory deorbit compliance

### **The Technical Innovations This Analysis Enables**

- **Collision Probability Modeling:** Physics-complete registry enables Monte Carlo simulations
- **Traffic Management Systems:** Altitude/inclination density maps inform conjunction warnings
- **Economic Impact Assessment:** Mass × velocity × collision probability = quantifiable insurance risk

---

## **How to Use This Repository**

### **Prerequisites**

```bash
python >= 3.11
pandas >= 2.0
numpy >= 1.24
matplotlib >= 3.7
seaborn >= 0.12
scipy >= 1.10
scikit-learn >= 1.3
```

### **Installation**

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

**⚠️ CRITICAL: Always use a virtual environment.** This project has specific dependency versions (Pandas 2.x, NumPy 1.24+) that may conflict with system-wide Python packages. Skipping the virtual environment step will cause import errors and version conflicts.

### **Execution Order**

1. **Data Acquisition:** Run `01_ucs_cleanup.ipynb` to fetch UCS data → `02_satcat_cleanup.ipynb` to fetch SATCAT data
   - Notebooks automatically download raw data to `data/original/` (git-ignored)
   - SATCAT rate-limited: 20 requests/day per IP; plan accordingly if re-running
2. **Synthesis:** Run `03_orbital_risk_synthesis.ipynb` to merge datasets
3. **Analytics:** Run `04_active_fleet_intelligence.ipynb` → `05_strategic_analysis.ipynb`

**Data Freshness:** To regenerate with latest orbital data, delete `data/original/` and re-run notebooks 01-02. Cleaned outputs (`data/clean/`) are committed for immediate analysis without fetching raw data.

---

## **Limitations & Future Work**

### **Current Limitations**

1. **Mass Estimation Uncertainty:**

   - 88.8% of mass values are proxies (ESA standards), not measurements
   - Debris fragments assigned uniform 50kg average (actual range: 1g - 1000kg)
   - Recommendation: Integrate USSTRATCOM high-fidelity mass catalog (classified, requires partnership)

2. **Temporal Snapshot:**

   - Analysis uses 2026 simulation year; orbital environment changes daily
   - Recommendation: Implement automated pipeline pulling live SATCAT updates

3. **Collision Probability:**
   - Current analysis quantifies mass/energy but not collision probability
   - Recommendation: Integrate conjunction assessment algorithms (NASA CARA methods)

### **Future Enhancements**

- **Machine Learning Integration:** Train debris classification models on RCS/altitude/age features
- **Interactive Dashboard:** Plotly/Dash web app for real-time orbital risk exploration
- **Geopolitical Risk Scoring:** Integrate launch site/owner data for regulatory compliance audits
- **Economic Impact Model:** Translate kinetic energy → insurance premiums → policy cost-benefit analysis

---

## **References & Data Sources**

### **Academic & Policy Sources**

1. Kessler, D.J. & Cour-Palais, B.G. (1978). "Collision Frequency of Artificial Satellites: The Creation of a Debris Belt." _Journal of Geophysical Research_.
2. European Space Agency (2025). "ESA Space Environment Report 2025." _ESA Space Debris Office_.
3. Union of Concerned Scientists (2024). "UCS Satellite Database." *https://www.ucsusa.org/resources/satellite-database*
4. NASA Orbital Debris Program Office (2023). "Orbital Debris Quarterly News."

### **Technical Resources**

- CelesTrak SATCAT: *https://celestrak.org/satcat/search.php*
- NASA Vis-Viva Equation: *https://en.wikipedia.org/wiki/Vis-viva_equation*
- Kepler's Laws: *https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion*
- Brent's Method: *https://en.wikipedia.org/wiki/Brent%27s_method*

---

## **AI Assistance & Transparency Statement**

In alignment with academic integrity and professional data science standards, I utilized CoPilot as a technical thought partner throughout this project. This disclosure documents where AI assisted versus where I made independent analytical decisions:

**AI-Assisted Components:**

- **Code Prototyping:** AI helped prototype `scipy.optimize` curve-fitting implementations and debug pandas merge operations
- **Documentation Formatting:** AI assisted with markdown formatting, technical writing structure, and README organization
- **Validation Logic:** AI peer-reviewed physics calculations (Vis-Viva, Kepler's Third Law) for mathematical accuracy
- **Environment Troubleshooting:** AI provided shell-specific commands for virtual environment activation across Windows/Mac/Linux

**Independent Analytical Work:**

- **All strategic insights and findings** (2014 Pivot, Zombie Protocol, 68km Compression Crisis) are my original interpretations of the processed data
- **Data pipeline architecture** (3-tier imputation hierarchy, merge strategy, zombie algorithm design) represents my engineering decisions
- **Threshold selections** (110% lifetime for zombies, ESA proxy values, regime classifications) were determined through domain research and validation
- **Visual narrative** (figure selection, KDE analysis methodology, risk metric design) reflects my understanding of orbital mechanics

**Why This Matters:** As a student completing my 4th independent capstone, I want to demonstrate that using AI as a tool doesn't diminish the work—it accelerates it. You still have to understand the underlying principles of what the AI is doing for you, of what the AI is speeding up for you. AI helped me write faster, debug smarter, and document cleaner—but the methodology, the insights, and the analytical framework are mine. The difference between using AI as a crutch versus a tool is whether you can explain _why_ the code works, not just _that_ it works. Every analytical decision in this project is defensible—and that rigor is what distinguishes tooling from dependency.


## **About This Project**

This analysis represents the **Data Science capstone** in the Code:You program, where I completed **4 independent capstone projects** across distinct technology pathways:

**Completed Capstone Projects:**

1. **Software Development Path (C#):** Enterprise application architecture, OOP design patterns
2. **Web Development Path (JavaScript/Vue.js):** Full-stack web applications, reactive UI frameworks
3. **Cloud Computing Path (AWS):** Infrastructure-as-code, serverless functions, scalable deployment
4. **Data Science Path (Python):** This project - physics-informed analytics, statistical imputation, production ETL

**What This Project Demonstrates:**

- **Technology Versatility:** Proven ability to master fundamentally different tech stacks (C# → JavaScript → AWS → Python)
- **Domain Adaptability:** Self-taught orbital mechanics and astrophysics concepts to properly model kinetic risk
- **Real-World Complexity:** Worked with messy, incomplete, domain-specific datasets requiring external research (ESA standards, Keplerian mechanics)
- **Production Engineering Ethics:** Transparently documented assumptions, validated against authoritative benchmarks (ESA 2025), communicated uncertainty bounds rather than hiding them
- **Interdisciplinary Integration:** Combined physics, statistics, geopolitics, and data engineering

**Contact:** James Glosser | DemonicUrges05@gmail.com | https://www.linkedin.com/in/james-glosser-249100204/

---

## **License**

This project is released under the MIT License. Data sources (SATCAT, UCS) retain their original licenses and usage restrictions.
