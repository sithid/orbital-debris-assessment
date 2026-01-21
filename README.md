# Orbital Clutter: Mapping the Kessler Acceleration

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### **Project Description**

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data with the **CelesTrak SATCAT Registry**, this analysis quantifies the **Visibility Gap** and evaluates the environment against the **Kessler Syndrome**—the tipping point where orbital collisions become a self-sustaining cascade.

### **Key Insights**

- **The 47.6% Zombie Blind Spot:** Analysis of the 'Visibility Gap' reveals that nearly half of all tracking failures are caused by **Inactive 'Zombie' Satellites**. This debunks the myth that small fragmentation is the primary driver of catalog uncertainty; the real risk is large, uncontrolled payloads drifting through commercial lanes.
- **The 2014 Great Kessler Acceleration:** Mathematical modeling identifies **2014** as the critical "Decoupling Point." Since this year, orbital growth has abandoned the linear 20th-century model and locked into an **Exponential Kessler Arc**.
- **The Kessler Clock (2.8-Year Doubling Time):** Tactical audits of the active fleet reveal a growth rate that doubles the orbital population every ~2.8 years. This velocity creates an "Active Kinetic Load" that outpaces legacy debris mitigation guidelines.
- **The 100% Density Achievement:** This project utilized **Physics-Informed Reconstruction** to achieve 100% data density across 20+ physical and orbital features for the active fleet, revealing the true kinetic energy of the "invisible" population.
- **The Kessler Canyon (LEO Concentration):** Spatial analysis confirms that risk is not evenly distributed; mass is acutely concentrating in the 500-600km LEO shell, creating a high-density corridor for potential cascade events.

---

### **Visualizing the Shift**

![The Strategic Synthesis](../../images/great_acceleration.png)
_Fig 1: The Strategic Synthesis showing the divergence between legacy linear expectations (Dashed Green) and the current exponential reality (Magenta)._

---

### **Analytical Strategy**

The analysis is structured as an **Intelligence Briefing** across two distinct phases:

1. **Phase 1: The Active Environment (`ucs_eda.ipynb`)**

   - Characterizing "High-Value" targets versus the commercial swarm.
   - Mapping the **Oligopoly of Orbit** (Top 10 Operators).
   - Establishing the mathematical proof of exponential acceleration.

2. **Phase 2: The Invisible Population (`satcat_eda.ipynb`)**
   - Auditing the 60,000-object Master Satellite Catalog.
   - Using Tier 1 Imputation to proxy the mass of spent rocket bodies and fragments.
   - Synthesizing active and inactive data to locate the "Collision Event Horizon."

---

### **AI Collaboration Disclosure**

This project utilized Generative AI to assist with specific engineering and analytical goals:

- **Mathematical Prototyping:** I collaborated with **Gemini** to prototype the `scipy.optimize` curve-fitting logic and the HUD-style visualization coordinate transforms for the Kessler Clock.
- **Data Engineering Audit:** I used AI to peer-review my **Physics Reconstruction Engine** and verify the accuracy of the grouped median imputation logic for missing mass data.
- **Technical Documentation:** I utilized AI to assist with text formatting for the intelligence briefings and to troubleshoot environment activation commands.

**Note:** All analytical decisions, data filtering thresholds (The Kessler Canyon), and strategic findings (The Great Acceleration) are my original conclusions based on the processed data.

---

### **Installation & Setup**

1. **Clone the repository.**
2. **Create and Activate the Virtual Environment:**
   - `python -m venv venv`
   - Activate: `source venv/Scripts/activate` (Mac/Linux) or `.\venv\Scripts\activate` (Windows)
3. **Install Dependencies:**
   - `pip install -r requirements.txt`
4. **Execution Order:**
   - **`ucs_cleanup.ipynb`**: Normalization & Physics Reconstruction (Active Satellites).
   - **`ucs_eda.ipynb`**: Active Fleet Characterization & Exponential Modeling.
   - **`satcat_cleanup.ipynb`**: SATCAT Merge & Debris Proxying (Tier 1 Imputation).
   - **`satcat_eda.ipynb`**: Final Intelligence Briefing.

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


