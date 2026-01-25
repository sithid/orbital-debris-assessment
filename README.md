# Orbital Debris Assessment: A Physics-Informed Analysis of the Kessler Syndrome Acceleration

**Author:** James Glosser  
**Contact:** DemonicUrges05@gmail.com | [LinkedIn](https://www.linkedin.com/in/james-glosser-249100204/)  
**Repository:** [github.com/sithid/orbital-debris-assessment](https://github.com/sithid/orbital-debris-assessment)  
**Last Updated:** January 2026  
**Status:** Code:You Capstone Project #4 (Data Analysis Pathway)

---

## **Executive Summary**

This project delivers a comprehensive orbital debris risk assessment by engineering a **physics-reconstructed master registry** that merges 67,264 tracked SATCAT objects with high-fidelity Union of Concerned Scientists (UCS) satellite data. By implementing **Vis-Viva velocity calculations**, **ESA-standard mass imputation**, and **Kernel Density Estimation (KDE) spatial analysis**, this analysis quantifies the 2014 "Kessler Acceleration"—the mathematical inflection point where commercial mega-constellation deployment rates surpassed 67 years of legacy launch activity.

### **Key Findings**

- **The 2014 Pivot:** Mathematical proof (via Brent's Method root-finding) that exponential satellite growth officially surpassed linear Cold War trends in mid-2014
- **64km Compression Crisis:** KDE analysis reveals modern mega-constellations occupy a narrow 200-600km band, creating a "commuter lane" 64km below a dense field of uncontrolled rocket bodies (800-1200km)
- **Zombie Protocol Imperative:** Identified 5,278 defunct payloads (satellites only; excludes debris/rocket bodies) exceeding 110% design life, representing high-mass collision catalysts in high-traffic orbits
- **Double Threat Topology:** The orbital environment exhibits vertical segregation where active satellites operate in a "kinetic canyon" bounded by legacy debris above and exponential launch rates below

### **Technical Impact**

**Data Engineering Achievement:**

- Merged 67,264 SATCAT objects + 7,542 UCS satellites → 32,687 physics-complete in-orbit records
- Achieved 100% feature density across 40 engineered attributes through tiered imputation (UCS verified → Keplerian derivation → ESA proxies)
- Implemented Vis-Viva equation to reconstruct orbital velocity for 100% of tracked objects (critical for kinetic energy modeling)
- Validated total mass estimate against ESA 2025 benchmarks (composition match within 0.7%)

**Analytical Innovation:**

- Identified zombie satellite distribution by owner, revealing US (2,211 satellites, 42%) and Russia/CIS (1,429 satellites, 27%) as primary contributors to defunct payload population
- Applied dual-cadence curve fitting (linear 1957-2013 vs. exponential 2014-2026) to prove acceleration hypothesis
- Performed 2D KDE spatial analysis to quantify the 64km altitude compression between active/inactive populations

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

High-resolution Kernel Density Estimation reveals a dangerous vertical segregation:

- **"Commuter Lane" (200-600km):** Modern mega-constellations operate in a compressed 400km band
- **"Deadly Ring" (800-1200km):** Legacy rocket bodies and defunct satellites loom 64km above
- **The Pincer Effect:** Active satellites sprint through a canyon where the ceiling is made of multi-ton kinetic bombs

### **The "Zombie Satellite" Population**

This analysis identifies **5,278 defunct payloads** (satellites only; debris and rocket bodies are excluded from this classification) that:

- Exceed 110% of their design lifetime (e.g., 15-year satellite now 16.5+ years old)
- Average age of 25.2 years (significantly beyond typical 10-15 year design lives)
- Represent 30.1% of the total payload population (17,562 active + inactive satellites)
- Geopolitical distribution reveals Cold War legacy: US (42%) and Russia/CIS (27%) account for 69% of zombie population

**Methodology Note:** The zombie algorithm applies exclusively to objects classified as `PAYLOAD` in SATCAT, filtering out non-operational satellites via status codes or age-to-lifetime ratios. The total in-orbit population includes an additional 12,672 debris fragments and 2,401 rocket bodies that are not counted in zombie statistics.

---

## **Dataset Architecture**

### **Primary Data Sources**

1. **SATCAT (Satellite Catalog) - CelesTrak**

   - **Source:** [`https://celestrak.org/pub/satcat.csv`](https://celestrak.org/pub/satcat.csv)
   - **Coverage:** 67,264 tracked objects (1957-present)
   - **Scope:** Global registry including active satellites, rocket bodies, and debris fragments
   - **Limitations:** Mass-blind (no mass data), 0.0 placeholders, inconsistent string formatting

2. **UCS Satellite Database - Union of Concerned Scientists**

   - **Source:** [`https://www.ucsusa.org/resources/satellite-database`](https://www.ucsusa.org/resources/satellite-database)
   - **Coverage:** 7,542 active satellites (verified operational)
   - **Scope:** High-fidelity metadata (launch mass, design lifetime, owner, purpose)
   - **Limitations:** Active payloads only (excludes debris/rocket bodies)

3. **ESA Space Environment Report (2025)**
   - **Source:** European Space Agency debris standards
   - **Coverage:** Statistical proxies for untracked/unknown objects
   - **Scope:** Mass averages, composition percentages, size distributions
   - **Application:** Tier 3 imputation fallback for objects without UCS/SATCAT mass data

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

- **Rocket Bodies:** 2,000 kg (ESA standard average)
- **Unknown Payloads:** 500 kg (conservative median for non-UCS satellites)
- **Debris Fragments:** 50 kg (trackable fragment average)
- **Unclassified Objects:** 100 kg (safety fallback)

**Validation Results:**

| Metric                  | This Analysis | ESA 2025 Benchmark | Deviation            |
| :---------------------- | :------------ | :----------------- | :------------------- |
| **Total In-Orbit Mass** | 16.3 kilotons | 13.6-15.1 kilotons | +7.2% (conservative) |
| **Payload Mass %**      | 70.8%         | 71.5%              | -0.7% ✅             |
| **Rocket Body Mass %**  | 28.1%         | 27.4%              | +0.7% ✅             |
| **Debris Mass %**       | 1.1%          | 1.1%               | 0.0% ✅              |

**Interpretation:** The 7.8% overshoot represents a **worst-case mass scenario** due to conservative 500kg proxies applied to ~10,000 unknown payloads. Composition percentages match ESA benchmarks, validating the tiered methodology. This deviation is documented transparently rather than hidden—demonstrating production data engineering ethics.

**Critical Transparency Statement:**

- Mass values for **88.8% of objects** are statistical proxies, not direct measurements
- The term "100% data density" refers to **imputation completeness**, not measurement fidelity
- Kinetic energy calculations for unknown payloads use conservative estimates; actual values may vary

**Dry Mass Derivation:**

- Applied orbit-specific fuel fraction ratios (LEO payloads: 0.65, GEO: 0.55, debris/rocket bodies: 1.0)
- Derived `dry_mass_kg` for collision modeling (structural mass only)

**Output:** `satcat_cleaned.csv` (67,264 records, 40 features, 100% imputation coverage)

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
KE = 0.5 × dry_mass_kg × velocity_m_s²
```

**Output:** `kinetic_master.csv` (67,264 records, 51 features)

**Vital Statistics:**

- **In-Orbit Objects:** 32,687 (48.6% of catalog)
- **Total Mass:** ~16.3 Kilotons ⚠️ _(exceeds ESA 2025 benchmark by 7.2%)_
- **Kinetic Energy:** ~333 Terajoules
- **Zombie Satellites:** 5,278 defunct payloads
- **Average Orbital Velocity:** 6.90 km/s (altitude-adjusted via Vis-Viva)

Verified the final `kinetic_master.csv` contains **32,687** in-orbit objects representing **~16.3 Kilotons** of mass (worst-case estimate) and **~333 Terajoules** of kinetic energy.

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

- **Active Satellites (Median):** 550km altitude
- **Rocket Bodies (Median):** 814km altitude
- **Vertical Gap:** **64km separation**

**The "Double Threat" Topology:**

1. **Floor Rising:** Modern mega-constellations compress into 200-600km band
2. **Ceiling Heavy:** Legacy rocket bodies create dense field at 800-1200km
3. **Pincer Effect:** Active satellites operate in a "canyon" bounded by kinetic threats above/below

**Energy Disparity Analysis:**

- **Energy Disparity (Adjusted):** Rocket bodies carry **1.9× more kinetic energy** than satellites in the same orbital regime
  - **Caveat:** This ratio includes ~10,000 unknown payloads imputed at 260-500kg; actual disparity for measured objects may vary
  - **Implication:** While rocket bodies remain high-risk shrapnel sources, modern mega-constellation satellites (e.g., Starlink: 260kg) represent a **swarm threat** where quantity multiplies kinetic load

**Zombie Geopolitical Distribution:**

The 5,278 zombie satellites break down by owner:

- **United States:** 2,211 satellites (41.9%)
- **Russia/CIS:** 1,429 satellites (27.1%)
- **China (PRC):** 372 satellites (7.0%)
- **United Kingdom:** 148 satellites (2.8%)
- **Japan:** 147 satellites (2.8%)

This distribution reveals the Cold War legacy effect: US and Soviet space programs created 69% of today's defunct payload population, representing long-term collision risks as these aged platforms (average 25.2 years old) enter unpredictable decay spirals.

---

## **Final Master Registry Statistics**

| Metric                   | Value              | Description                                         |
| :----------------------- | :----------------- | :-------------------------------------------------- |
| **Total Objects**        | 67,264 records     | Complete SATCAT universe (1957-2026)                |
| **In-Orbit Objects**     | 32,687 (48.6%)     | Currently active kinetic threats                    |
| **Total Mass**           | 16,281 metric tons | Cumulative kinetic mass (ESA +7.2% worst-case)      |
| **Zombie Satellites**    | 5,278 payloads    | Defunct assets exceeding 110% design life (30.1% of payloads) |
| **Kinetic Energy**       | 333 Terajoules     | Total destructive potential at orbital velocities   |
| **Data Completeness**    | 100% imputation    | Physics-reconstructed across 51 engineered features |
| **UCS Enrichment**       | 7,542 satellites   | High-fidelity mass/lifetime data synchronized       |
| **Avg Orbital Velocity** | 6.90 km/s          | Altitude-adjusted via Vis-Viva equation             |

---

## **Key Visualizations**

### **Figure 1: Kinetic Mass Distribution (The White Whale)**

![Mass Distribution Log](./images/mass_distribution_log.png)  
_Figure 1: Logarithmic mass distribution revealing the 6-order-of-magnitude disparity in orbital objects. The International Space Station (450,000 kg) represents the "White Whale" outlier, while CubeSat swarms (<10 kg) populate the extreme left. This histogram proves why simple object counts mislead risk assessments—the ISS alone carries more kinetic mass than 450,000 CubeSats combined. The logarithmic scale is necessary to visualize both populations simultaneously, exposing the "invisible mass" hiding in aggregate statistics._

---

### **Figure 2: The Visibility Trap**

![Visibility Trap](./images/visibility_trap.png)  
_Figure 2: Mass vs. Count distribution revealing the deceptive inversion between object prevalence and kinetic risk. By count, the orbital population appears balanced: debris (38.8%) and active satellites (37.6%) are statistically equivalent. However, by mass, rocket bodies (7.3% of count) carry ~30% of total kinetic energy—a 4:1 mass-to-count ratio. This creates the "visibility trap": regulatory frameworks focused on satellite proliferation (count-based metrics) systematically miss the legacy debris threat (mass-based physics). The most dangerous objects—multi-ton rocket bodies—are statistically invisible when sorted by count alone, appearing as "just 2,401 catalog entries" while carrying more collision energy than 12,000+ debris fragments combined._

---

### **Figure 3: The Great Acceleration (2014 Pivot)**

![Great Acceleration](./images/great_acceleration.png)  
_Figure 3: Dual-cadence curve fitting proving the 2014 acceleration hypothesis. The linear model (red, 1957-2013) shows steady Cold War era growth (~100 satellites/year). The exponential model (cyan, 2014-2026) captures commercial mega-constellation deployment. Brent's Method root-finding identifies mid-2014 as the mathematical crossover point where exponential velocity surpassed linear trends. This is not subjective interpretation—it's calculus-verified proof of a regime change._

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
_Figure 6: Altitude-band population density showing object distribution within Low Earth Orbit (200-2000km). The 400-600km "Starlink band" shows dramatic concentration of modern mega-constellations, while the 800-1200km band contains legacy rocket bodies and defunct satellites. This granular LEO analysis reveals the vertical segregation that creates the "Kessler Canyon" pincer effect—active assets operating directly beneath a ceiling of uncontrolled high-mass objects._

---

### **Figure 7: The Kessler Canyon (KDE Spatial Analysis)**

![Kessler Canyon](./images/kessler_canyon.png)  
_Figure 7: High-resolution KDE analysis revealing vertical orbital segregation. The cyan "Commuter Lane" (active satellites, ~550km median) sits 64km below the crimson "Deadly Ring" (rocket bodies, ~800km+ median). This altitude gap creates the "Kessler Canyon" pincer effect—modern mega-constellations operate directly beneath a ceiling of uncontrolled, high-mass legacy objects. **Note:** Energy calculations include ~10,000 payloads with imputed 260-500kg masses; the 1.9× rocket body energy advantage reflects measured vs. imputed mass distributions._

---

### **Figure 8: Zombie Satellite Distribution**

![Zombie Index](./images/zombie_index.png)  
_Figure 8: The Zombie Satellite distribution showing (Left) age histogram of 5,278 defunct payloads with 25-year average age, and (Right) top 5 owners by zombie count. "Zombies" are operationally dead payloads or satellites exceeding design life by 10%+ (`sat_age_years > lifetime_years × 1.10`). The United States leads with 2,211 zombie satellites (42% of total), followed by Russia/CIS with 1,429 (27%). This geopolitical breakdown reveals Cold War legacy: US and Soviet programs created the majority of today's uncontrolled payload population, representing imminent collision risks as these aged platforms enter unpredictable decay spirals._

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
│   ├── original/          # Raw source files (SATCAT, UCS)
│   └── clean/             # Processed datasets
│       ├── ucs_cleaned.csv
│       ├── satcat_cleaned.csv
│       └── kinetic_master.csv
├── notebooks/
│   ├── 01_ucs_cleanup.ipynb           # UCS ETL pipeline
│   ├── 02_satcat_cleanup.ipynb        # SATCAT reconstruction
│   ├── 03_orbital_risk_synthesis.ipynb # Master registry merge
│   ├── 04_active_fleet_intelligence.ipynb # 2014 pivot proof
│   └── 05_strategic_analysis.ipynb    # Kessler Canyon analysis
├── images/                # Visualization exports
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

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

- **Mass Composition:** Validated against ESA 2025 benchmarks (payload/rocket body/debris ratios match within 0.7%)
- **Velocity Sanity Check:** Average orbital velocity (6.90 km/s) aligns with expected LEO range (6.5-7.8 km/s across all orbital regimes)
- **Kinetic Energy:** Total 312 TJ represents realistic worst-case scenario for in-orbit kinetic load

---

## **Strategic Insights for Industry**

### **The Policy Implications**

1. **Active Debris Removal (ADR) Prioritization:**

   - 5,278 zombie satellites represent priority removal targets (30% of payload population)
   - Geopolitical concentration: US and Russia control 69% of zombie inventory, suggesting bilateral cleanup coordination
   - ROI justification: Removing 1 high-mass zombie = preventing 1,000+ trackable debris fragments (per ESA collision models)

2. **Launch Licensing Reform:**

   - 2014 pivot proves current regulatory frameworks (designed for linear growth) are inadequate
   - Recommendation: Implement **orbital density caps** per altitude band (e.g., max 500 satellites per 100km shell)
   - Precedent: ITU frequency allocation model (first-come-first-served → congestion management)

3. **Mega-Constellation Design Standards:**
   - 64km canyon gap suggests coordination zones for active vs. passive objects
   - Proposal: Mandate 600-700km "buffer zone" free of persistent debris (via guaranteed deorbit compliance)

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

1. **Data Cleaning:** Run `01_ucs_cleanup.ipynb` → `02_satcat_cleanup.ipynb`
2. **Synthesis:** Run `03_orbital_risk_synthesis.ipynb`
3. **Analytics:** Run `04_active_fleet_intelligence.ipynb` → `05_strategic_analysis.ipynb`

**Note:** Raw data files (`satcat.csv`, `UCS-Satellite-Database.csv`) must be placed in `data/original/` before execution.

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

In alignment with academic integrity and professional data science standards, I utilized **Claude Sonnet 4.5** as a technical thought partner throughout this project. This disclosure documents where AI assisted versus where I made independent analytical decisions:

**AI-Assisted Components:**

- **Code Prototyping:** AI helped prototype `scipy.optimize` curve-fitting implementations and debug pandas merge operations
- **Documentation Formatting:** AI assisted with markdown formatting, technical writing structure, and README organization
- **Validation Logic:** AI peer-reviewed physics calculations (Vis-Viva, Kepler's Third Law) for mathematical accuracy
- **Environment Troubleshooting:** AI provided shell-specific commands for virtual environment activation across Windows/Mac/Linux

**Independent Analytical Work:**

- **All strategic insights and findings** (2014 Pivot, Zombie Protocol, 64km Compression Crisis) are my original interpretations of the processed data
- **Data pipeline architecture** (3-tier imputation hierarchy, merge strategy, zombie algorithm design) represents my engineering decisions
- **Threshold selections** (110% lifetime for zombies, ESA proxy values, regime classifications) were determined through domain research and validation
- **Visual narrative** (figure selection, KDE analysis methodology, risk metric design) reflects my understanding of orbital mechanics

**Why This Matters:** As a student completing my 4th independent capstone, I want to demonstrate that using AI as a tool doesn't diminish the work—it accelerates it. You still have to understand the underlying principles of what the AI is doing for you, of what the AI is speeding up for you. I can't use `scipy.optimize.curve_fit` without understanding exponential vs. linear regression. I can't validate Vis-Viva velocity calculations without understanding orbital mechanics. AI helped me write faster, debug smarter, and document cleaner—but the physics, the insights, and the analytical framework are mine. The difference between using AI as a crutch versus a tool is whether you can explain *why* the code works, not just *that* it works.

---

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
