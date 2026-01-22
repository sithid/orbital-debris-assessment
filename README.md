# Orbital Clutter: Mapping the Kessler Acceleration

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### **Project Description**

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data with the **CelesTrak SATCAT Registry**, this analysis quantifies the **Visibility Gap** and evaluates the environment against the **Kessler Syndrome**—the tipping point where orbital collisions become a self-sustaining cascade.

### **Key Insights**

- **The 47.6% Zombie Blind Spot:** Analysis of the 'Visibility Gap' reveals that nearly half of all tracking failures are caused by **Inactive 'Zombie' Satellites**. This debunks the myth that small fragmentation is the primary driver of catalog uncertainty; the real risk is large, uncontrolled payloads drifting through commercial lanes.
- **The 2014 Great Kessler Acceleration:** Mathematical modeling identifies **2014** as the critical "Decoupling Point." Since this year, orbital growth has abandoned the linear 20th-century model and locked into an **Exponential Kessler Arc**, tripling in velocity due to commercial proliferation.
- **The Kessler Clock (2.8-Year Doubling Time):** Tactical audits of the active fleet reveal a growth rate that doubles the orbital population every ~2.8 years. This velocity creates an "Active Kinetic Load" that outpaces legacy debris mitigation guidelines.
- **The 100% Density Achievement:** This project utilized **Physics-Informed Reconstruction** to achieve 100% data density across 20+ physical and orbital features for the active fleet, revealing the true kinetic energy of the "invisible" population.
- **The Kessler Canyon (Orbital Segregation):** KDE analysis reveals a distinct segregation of risk. While active satellites cluster in the "Commuter Lane" (~550km), massive abandoned rocket bodies form a permanent "Deadly Ring" at ~900km.

---

### **Visualizing the Crisis**

#### **1. The Intelligence Gallery (Phase 1: Active Environment)**

**The Geospatial Hegemony Shift**
![Hegemony Map](images/geospatial_shift.png)

_Figure 1: Mapping the physical control of orbital space. This audit tracks the transition from state-actor dominance to a multi-polar commercial landscape, identifying the geographical origins of the kinetic load._

**The Oligopoly of Orbit**
![Operator Oligopoly](images/operator_oligopoly.png)

_Figure 2: Identification of the specific entities driving the commercial surge. This visual highlights how a handful of "Commercial Titans" now control the majority of active LEO assets._

**Kinetic Mass Profiling (The Swarm vs. The Giants)**
![Mass Profile](images/mass_distribution_log.png)

_Figure 3: Logarithmic scaling of the active fleet. In a collision event, mass equates to "shrapnel potential"; this identifies "High-Value" targets versus the CubeSat swarm._

**Vertical Congestion (LEO vs. The Rest)**
![Orbit Congestion](images/orbit_congestion_leo.png)

_Figure 4: Mapping the "Shell of Density." This chart proves that exponential growth is almost exclusively contained within the 500-600km LEO corridor._

---

#### **2. The Strategic Synthesis (Phase 2 & 3: Global Risk)**

**The Great Kessler Acceleration (2014 Pivot)**
![Great Acceleration](images/great_acceleration.png)

_Figure 5: The "Decoupling Point." This definitive synthesis identifies 2014 as the pivot year where orbital growth locked into an exponential arc, outpacing legacy debris mitigation guidelines._

**The Kessler Canyon (Orbital Segregation)**
![Kessler Canyon](images/kessler_traffic_map.png)

_Figure 6: Segregation of risk. While active satellites cluster in the "Commuter Lane" (~550km), massive abandoned rocket bodies form a permanent "Deadly Ring" at ~900km._

---

## **Current Pipeline Architecture: The Gold Standard**

The project has transitioned from raw data ingestion to a **Physics-Complete** environment. We utilize a "Hierarchy of Truth" methodology to ensure the highest possible fidelity for kinetic modeling.

### **1. Data Cleaning & Density Engineering**
* **UCS Cleanup (`ucs_cleanup.ipynb`):** * Sanitized 7,500+ active satellites.
    * Implemented orbit-specific *Dry-to-Wet* mass ratios.
    * Engineered multi-sector Boolean flags (Military, Commercial, Civil, Gov).
* **SATCAT Cleanup (`satcat_cleanup.ipynb`):**
    * Reconstructed a 60,000+ object global registry.
    * **Keplerian Engine:** Derived missing orbital periods via Kepler’s Third Law.
    * **High-Fidelity Enrichment:** 1:1 integration with UCS data to repair SATCAT "Mass Blindness."
    * **Tiered Imputation:** Applied ESA-standard mass proxies for debris and rocket bodies.
    * **Temporal Hardening:** Implemented `Int64` nullable integers for object age relative to Simulation Year 2026.
* **The "Hierarchy of Truth" Integration:** 
    * Implemented a multi-tier data repair logic where verified UCS observations (Tier 1) are used to "patch" missing SATCAT geometry (Period, Inclination, Altitudes) before resorting to mathematical derivation (Tier 2).
* **Kinetic Risk Modeling:**
    * Developed a hybrid vulnerability model using specific UCS design-life metrics where available, falling back to a 15-year industry standard proxy for "Ghost" payloads.

### **2. Current Project Status**
* [x] **Phase 1: Foundation** (UCS & SATCAT Standardization) - **100% Complete**
* [ ] **Phase 2: Synthesis** (Risk Integration & Zombie Identification) - **CURRENT FOCUS**
  * _Merging Intelligence:_ 1:1 coupling of `ucs_cleaned` and `satcat_cleaned`.
  * _Kinetic Energy Modeling:_ Applying $E_k = \frac{1}{2}mv^2$ to 60,000+ objects using orbital velocity vectors.
* [ ] **Phase 3: Strategic Analysis** (Geopolitical Risk & EoL Modeling) - **PENDING**

---

## **Technical Standards**

- **Primary Key:** `norad_id` (Standardized String)
- **Mass Metric:** `proxy_mass_kg` (Launch/Wet Mass) and `dry_mass_kg` (Structural Mass)
- **Simulation Baseline:** Year 2026
- **Physics Units:** km (Altitude), minutes (Period), degrees (Inclination), m² (RCS)

### **Key Feature Glossary**

#### **1. Physical & Orbital Registry (SATCAT Derived)**

| Feature         | Meaning                                                                               |
| :-------------- | :------------------------------------------------------------------------------------ |
| `proxy_mass_kg` | The "Wet Mass" (Launch) used for initial kinetic energy calculations.                 |
| `dry_mass_kg`   | The estimated "Structural Mass" used for end-of-life impact modeling (Stage 5.2).     |
| `rcs_class`     | Geometric size category (Small, Medium, Large) derived from radar cross-section data. |
| `in_orbit`      | Binary flag (1/0) isolating current kinetic threats from decayed historical records.  |
| `owner_code`    | Standardized ISO-style country/entity code for geopolitical risk aggregation.         |
| `orbit_class`   | Standardized regime (LEO, MEO, GEO, Elliptical) for spatial congestion analysis.      |

#### **2. Fleet Intelligence & Sector Flags (UCS Derived)**

| Feature          | Meaning                                                                                     |
| :--------------- | :------------------------------------------------------------------------------------------ |
| `is_zombie`      | (Phase 2) Boolean flag identifying payloads that are inactive or have exceeded design life. |
| `is_military`    | Boolean flag identifying state-actor defense assets.                                        |
| `is_commercial`  | Binary flag identifying assets owned/operated by private entities for profit.               |
| `is_government`  | Binary flag identifying assets owned by state agencies (e.g., NASA, ESA).                   |
| `is_civil`       | Binary flag identifying academic, scientific, or amateur-led missions.                      |
| `lifetime_years` | Design-life expectancy used to calculate the "End-of-Life" risk threshold.                  |

---

### **AI Attribution & Usage Disclosure**

In alignment with professional data science standards, I utilized the **Gemini** model family as a technical thought partner. I targeted my usage of AI toward specific engineering and analytical goals:

- **Mathematical Prototyping:** I collaborated with AI to prototype the `scipy.optimize` curve-fitting logic and the HUD-style visualization coordinate transforms for the Kessler Clock.
- **Data Engineering Audit:** I used AI to peer-review my **Physics Reconstruction Engine** and verify the accuracy of the grouped median imputation logic.
- **Technical Documentation:** I utilized AI to assist with text formatting for the intelligence briefings and to troubleshoot shell-specific environment activation commands.

**Note:** All analytical decisions, data filtering thresholds (The Kessler Canyon), and strategic findings (The Great Acceleration) are my original conclusions based on the processed data.

---

### **Installation & Setup**

To ensure the analysis runs with the correct library versions, please use a virtual environment. This prevents dependency conflicts and ensures the mathematical models and visualizations render as intended.

1. **Clone the repository and navigate to the project root.**
2. **Create and Activate the Virtual Environment:**
   - Create: `python -m venv venv`
   - Activate - Windows (Git Bash): `source venv/Scripts/activate`
   - Activate - Windows (Command Prompt): `.\venv\Scripts\activate`
   - Activate - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - Activate (Mac/Linux): `source venv/bin/activate`
3. **Install Project Dependencies:** `pip install -r requirements.txt`
4. **Data Verification:** Ensure raw data files are in `data/original/` and cleaned outputs are directed to `data/clean/`.
5. **Execution Order:**
   - **`ucs_cleanup.ipynb`**: Cleans and reconstructs the active satellite database.
   - **`satcat_cleanup.ipynb`**: Normalizes the global satellite catalog and filters for current objects.
   - **`orbital_risk_synthesis.ipynb`**: Merges both cleaned datasets to create the `kinetic_master.csv`.
   - **`active_fleet_intelligence.ipynb`**: Explores the active fleet and calculates the Kessler Clock.
   - **`strategic_analysis.ipynb`**: Final high-level analysis of the global kinetic environment.

---

### **License**

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

**You are free to:**
- **Share** — copy and redistribute the material in any medium or format.
- **Adapt** — remix, transform, and build upon the material.

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial** — You may **NOT** use the material for commercial purposes. This includes selling the code, charging for access to the analysis, or using the models within a commercial product or service.

---

