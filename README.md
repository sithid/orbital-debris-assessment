# Orbital Clutter: Analyzing the Pollution of LEO

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### Project Description

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data from the **Union of Concerned Scientists (UCS)** with the **CelesTrak SATCAT**, this analysis quantifies the **Visibility Gap** and evaluates the environment against the **Kessler Syndrome**—the tipping point where orbital collisions become self-sustaining.

### Key Insights

- **The 50% Visibility Gap:** Nearly half of all objects with "unhealthy" tracking status (e.g., NEA - No Elements Available) are intact Inactive Satellites. These "Zombie Satellites" represent massive, unmonitored kinetic risks.
- **Active Satellite Trends (UCS Data):** Analysis of the UCS dataset reveals the explosion of commercial "Mega-Constellations." By visualizing satellite purposes and operators, this project identifies which sectors are contributing most to LEO density.
- **Evidence of Kessler Syndrome:** Analysis of LEO population trends shows a transition from linear growth to an exponential curve, punctuated by catastrophic fragmentation events in 2007 and 2009.
- **The 82.8% Mass Transparency Gap:** While tracking 32,000+ objects, high-fidelity mass data is only available for ~17% of the catalog. By merging UCS and SATCAT data, this project identifies that over 80% of the mass in orbit is "invisible" to standard analysis.
- **The "Kessler Canyon" (Orbital Segregation):** KDE analysis reveals a distinct segregation of risk in LEO. While active satellites cluster in the "Commuter Lane" (~550km), massive abandoned rocket bodies form a permanent "Deadly Ring" at ~900km. This creates a high-mass "canyon walls" effect, where the heaviest debris looms directly above modern infrastructure.


---

### Technical Highlights

- **Tier 1 Synthetic Mass Modeling:** Implemented categorical mass fills (e.g., 2,000kg for Rocket Bodies) to scientifically bridge the 82.8% data gap, converting a "Transparency Gap" into a actionable proxy model.
- **Growth Modeling:** Applied mathematical best-fit curves to distinguish between linear launch rates and exponential debris accumulation.
- **Multi-Dataset Visualization:** Created comparative plots using UCS data to show the ratio of commercial vs. government payloads and their intended orbital classes.
- **Boolean Masking:** Isolated "unhealthy" tracking flags to identify which object categories pose the greatest risk to orbital situational awareness.
- **Data Merging:** Integrated disparate datasets via **NORAD IDs** to separate active infrastructure from historical clutter.
- **Categorical Proportions:** Utilized pie charts and grouped counts to visualize the dominance of dead payloads in the tracking catalog.
- **Relational Data Mapping:** Cross-dataset lookup table using NORAD IDs to bridge the Union of Concerned Scientists (UCS) mass metrics with the CelesTrak orbital catalog.
- **Dual-Axis Trend Analysis:** Developed synchronized visualizations to compare the growth of orbital population (count) against cumulative mass (kg) to identify and visualize shifts in orbital density.

---

### Data Sources

- **Union of Concerned Scientists (UCS):** In-depth records of active satellites (Owner, Purpose, Mass, Orbit).
- **CelesTrak (NORAD/SATCAT):** Historical catalog of all man-made objects ever launched and their current tracking statuses.

---

### **Project Visualizations**

#### **1. The Kessler Growth Curve**

This chart demonstrates the transition from linear orbital growth to the current exponential "Hockey Stick" curve.
![Kessler Growth Curve](images/kessler_growth_curve.png)

#### **2. The Baseline: Known Mass in Orbit**

This visualization tracks the "Kinetic Fuel" (Mass) currently in orbit based strictly on public records. It establishes the baseline for our analysis before modeling the missing data.
![Cumulative Mass Curve](images/cumulative_mass_curve.png)

#### **3. The Kessler Reality Check: Modeled vs. Public Data**

Here we compare the public baseline (Blue) against our **Tier 1 Synthetic Model** (Red). The discrepancy visually proves the **82.8% Mass Transparency Gap**, revealing thousands of tons of "Hidden" orbital mass.
![The Kessler Reality Check](images/kessler_reality_check.png)

#### **4. The Double Threat: Population vs. Mass Accumulation**

This dual-axis visualization reveals the critical relationship between the number of orbital objects and the total kinetic "fuel" (mass) in orbit. While the population count (blue) shows the crowding of space, the cumulative mass (red) identifies the total energy available for a potential Kessler cascade.

![The Double Threat: Population vs. Mass](images/double_threat.png)

_Note: This chart utilizes the **Tier 1 Synthetic Mass Model** to show the most realistic correlation between congestion and kinetic potential._

### Visualizing the Threat

![Orbital Traffic Map](images/kessler_traffic_map.png)

_Figure: The "Orbital Traffic Map" reveals distinct highways of risk. The Green Peak represents the active economy (Starlink/OneWeb), while the Red Peak represents the "Ghost Town" of abandoned Soviet and US rocket stages._

---

### Stretch Goals & Future Roadmap: Collision Risk Assessment

While this project quantifies man-made orbital congestion, the ultimate goal is to evaluate the relative risk to modern space infrastructure.

**Upcoming Analysis: Man-Made vs. Natural Hazard Flux**
Current research indicates that for the first time in history, the risk of satellite failure due to man-made debris has surpassed the risk from natural meteoroids. I plan to integrate a "Flux Comparison" analysis using NASA’s Meteoroid and Orbital Debris (MMOD) estimates.

**Proposed To-Do List:**

- [ ] **Tier 2: RCS-Based Kinetic Modeling:** Utilize Radar Cross Section (RCS) data to calculate specific mass estimates for debris fragments based on their radar signature.
- [ ] **Comparative Velocity Modeling:** Visualize the kinetic energy difference between natural meteoroids (~20 km/s) and man-made orbital debris (~7.8 km/s).
- [ ] **Density Threshold Mapping:** Create a "Kessler Limit" overlay to show exactly where man-made density exceeds the background natural environment.
- [ ] **Risk Attribution:** Quantify the probability of a "Mission Ending Strike" from a 1cm man-made fragment versus a natural micrometeoroid of the same size.
- [ ] **Predictive Tracking Decay:** Use Correlation Matrices to determine if object age is a leading indicator for "unhealthy" tracking status.
- [ ] **Physical Risk Modeling:** Utilize RCS (Radar Cross Section) data to calculate the specific collision probability of "Zombie Satellites" versus standard debris fragments.
- [ ] **Geospatial Ground-Track Mapping:** Integrate `GeoPandas` to project orbital paths onto terrestrial maps, identifying high-density flyover zones for inactive debris.

---

### Installation & Setup

1. Clone the repository.
2. Ensure data files are in `data/original/` and `data/clean/`.
3. **Execution Order:**
   - Run `ucs_cleanup.ipynb` (Standardizing UCS records)
   - **`satcat_cleanup.ipynb` (The Cleaning Pipeline):**
     - **Tier 1 (Mass Imputation):** Uses ESA proxies to fill the 82.8% mass gap for Rocket Bodies and inactive payloads.
     - **Tier 2 (Physics Standardization):** Sanitizes RCS (Radar Cross Section) and orbital geometry to prepare for kinetic energy modeling.
   - Run `ucs_eda.ipynb` (Visualizing active satellite distribution and ownership)
   - Run `satcat_eda.ipynb` (Main Analysis: Debris, Growth, and Tracking Health)

---

### License

This project is licensed under the MIT License.
