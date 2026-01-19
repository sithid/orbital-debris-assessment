# Orbital Clutter: Mapping the Kessler Acceleration

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### **Project Description**

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data with the **CelesTrak SATCAT Registry**, this analysis quantifies the **Visibility Gap** and evaluates the environment against the **Kessler Syndrome**—the tipping point where orbital collisions become a self-sustaining cascade.

### **Key Insights**

- **The 47.6% Zombie Blind Spot:** Analysis of the 'Visibility Gap' reveals that nearly half of all tracking failures are caused by **Inactive 'Zombie' Satellites**. This debunks the myth that small fragmentation is the primary driver of catalog uncertainty; the real risk is large, uncontrolled payloads drifting through commercial lanes.
- **The 2014 Great Kessler Acceleration:** Mathematical modeling identifies **2014** as the critical "Decoupling Point." Since this year, orbital growth has abandoned the linear 20th-century model and locked into an **Exponential Kessler Arc**, tripling in velocity due to commercial proliferation.
- **The 82.8% Mass Transparency Gap:** While tracking 32,000+ objects, high-fidelity mass data is only available for ~17% of the catalog. This project utilized **Tier 1 ESA Proxy Imputations** to reclaim 80% of this data, revealing the true kinetic energy of the "invisible" fleet.
- **The Kessler Canyon (Orbital Segregation):** KDE analysis reveals a distinct segregation of risk. While active satellites cluster in the "Commuter Lane" (~550km), massive abandoned rocket bodies form a permanent "Deadly Ring" at ~900km.

---

### **Visualizing the Crisis**

#### **1. The Mass Gap (Tier 1 Analysis)**

![Kessler Reality Check](images/kessler_reality_check.png)
_The "Reality Check" reveals the 82.8% Mass Gap. The red area represents the massive amount of "Hidden" kinetic fuel identified through ESA proxy modeling._

#### **2. The Double Threat: Population vs. Kinetic Fuel**

![Double Threat](images/double_threat.png)
_A dual-axis synthesis of the crisis. While the Population (Blue) is exploding exponentially post-2014, the total Kinetic Mass (Red) continues its steady, dangerous climb, creating a pincer maneuver of risk._

#### **3. The Kessler Canyon (The Traffic Map)**

![Kessler Traffic Map](images/kessler_traffic_map.png)
_Mapping the physical highways of risk. This Kernel Density Estimation (KDE) shows the dangerous proximity between the high-density "Commuter Lane" and the high-mass "Deadly Ring" above it._

---

### **Scientific Methodology**

#### **1. Kinetic Risk: Closing the Mass Transparency Gap**

We rejected the "Drop all Nulls" approach. Instead, we developed a cleaning pipeline that utilizes **ESA (European Space Agency) Mass Proxies** to impute values for Rocket Bodies and Inactive Payloads based on standardized launch vehicle specifications.

#### **2. Temporal Modeling: The Kessler Engine**

Using `scipy.optimize`, we fitted historical growth data against both Linear and Exponential models. This mathematically validated the **2014 Pivot**, proving the environment has entered a self-accelerating phase.

---

### **Installation & Setup**

1. Clone the repository.
2. Ensure data files are in `data/original/` and `data/clean/`.
3. **Execution Order:**
   - `ucs_cleanup.ipynb` -> `ucs_eda.ipynb`
   - `satcat_cleanup.ipynb` (Tier 1 & Tier 2 Pipelines)
   - `satcat_eda.ipynb` (Main Briefing)
