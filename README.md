# Orbital Clutter: Analyzing the Pollution of LEO

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### Project Description

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data from the **Union of Concerned Scientists (UCS)** with the **CelesTrak SATCAT**, this analysis quantifies the **Visibility Gap** and evaluates the environment against the **Kessler Syndrome**—the tipping point where orbital collisions become self-sustaining.

### Key Insights

- **The "Kessler Canyon" (Orbital Segregation):** KDE analysis reveals a distinct segregation of risk in LEO. While active satellites cluster in the "Commuter Lane" (~550km), massive abandoned rocket bodies form a permanent "Deadly Ring" at ~900km. This creates a high-mass "canyon walls" effect, where the heaviest debris looms directly above modern infrastructure.
- **The 82.8% Mass Transparency Gap:** While tracking 32,000+ objects, high-fidelity mass data is only available for ~17% of the catalog. By merging UCS and SATCAT data, this project identifies that over 80% of the mass in orbit is "invisible" to standard analysis.
- **The 2014 Great Kessler Acceleration:** Modeling of the UCS dataset identifies **2014** as the critical mathematical inflexion point. At this moment, the exponential "New Space" growth rate officially outpaced the legacy linear trend, signaling a fundamental regime shift in orbital density.
- **The Exponential Risk Surplus:** The divergence between historical trends and modern growth reveals a "Risk Surplus" of thousands of active payloads. This volume of assets is pulling away from historical management models at an accelerating rate, increasing the active-on-active collision risk.
- **The 50% Visibility Gap:** Nearly half of all objects with "unhealthy" tracking status (e.g., NEA - No Elements Available) are intact Inactive Satellites. These "Zombie Satellites" represent massive, unmonitored kinetic risks.

### Visualizing the Crisis

#### 1. The Mass Gap (Tier 1 Analysis)
![Kessler Reality Check](images/kessler_reality_check.png)

_Figure: The "Reality Check" reveals the 82.8% Mass Gap. The grey area represents the massive amount of kinetic energy (rocket bodies/dead satellites) that raw public data fails to account for._

#### 2. The Great Kessler Acceleration (Tier 1 Analysis)
![Great Acceleration](images/great_acceleration.png)

_Figure: The "Acceleration Point" identifies the 2014 pivot. It highlights the "Exponential Risk Surplus"—the shaded delta between business-as-usual historical growth and the current commercial reality._

#### 3. The Double Threat: Legacy Mass vs. Exponential Proliferation
![Double Threat](images/double_threat.png)

_Figure: The "Double Threat" Synthesis overlays Legacy Risk (untracked high-mass debris) with Modern Risk (exponential active growth). It illustrates LEO caught in a "pincer maneuver" between abandoned heavy-lift hardware and a rapidly densifying commercial economy._

#### 4. The Kessler Canyon (Tier 2 Analysis)
![Orbital Traffic Map](images/kessler_traffic_map.png)

_Figure: The "Orbital Traffic Map" reveals distinct highways of risk: the Green Peak (Starlink Economy) sits directly below the Red Peak (The Rocket Body Graveyard)._

---

### Future Goals: The Advanced Analysis (`adv_analysis.ipynb`)

With the "Input Rate" for active satellites established, the next phase focuses on **Kinetic Threat Modeling** by merging active assets with the "Invisible Population" found in the SATCAT:

- [ ] **Density Threshold Mapping:** Create a "Kessler Limit" overlay to show exactly where man-made density exceeds the background natural environment.
- [ ] **Risk Attribution:** Quantify the probability of a "Mission Ending Strike" from a 1cm man-made fragment versus a natural micrometeoroid.
- [ ] **Predictive Tracking Decay:** Use Correlation Matrices to determine if object age is a leading indicator for "unhealthy" tracking status.
- [ ] **Physical Risk Modeling:** Utilize RCS (Radar Cross Section) data to calculate the specific collision probability of "Zombie Satellites".

---

### Installation & Setup

1. Clone the repository.
2. Ensure data files are in `data/original/` and `data/clean/`.
3. **Execution Order:**
   - Run `ucs_cleanup.ipynb` (Standardizing UCS records)
   - Run `ucs_eda.ipynb` (Modeling the 2014 Acceleration Point and active "Risk Surplus")
   - **`satcat_cleanup.ipynb` (The Cleaning Pipeline):**
     - **Tier 1 (Mass Imputation):** Uses ESA proxies to fill the 82.8% mass gap.
     - **Tier 2 (Physics Standardization):** Sanitizes RCS and orbital geometry for kinetic modeling.
   - Run `satcat_eda.ipynb` (Main Analysis: Debris, Growth, and Tracking Health)

---

### License
This project is licensed under the MIT License.