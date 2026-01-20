# Orbital Clutter: Mapping the Kessler Acceleration

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### **Project Description**

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data with the **CelesTrak SATCAT Registry**, this analysis quantifies the **Visibility Gap** and evaluates the environment against the **Kessler Syndrome**—the tipping point where orbital collisions become a self-sustaining cascade.

### **Key Insights**

- **The 47.6% Zombie Blind Spot:** Analysis of the 'Visibility Gap' reveals that nearly half of all tracking failures are caused by **Inactive 'Zombie' Satellites**. This debunks the myth that small fragmentation is the primary driver of catalog uncertainty; the real risk is large, uncontrolled payloads drifting through commercial lanes.
- **The 2014 Great Kessler Acceleration:** Mathematical modeling identifies **2014** as the critical "Decoupling Point." Since this year, orbital growth has abandoned the linear 20th-century model and locked into an **Exponential Kessler Arc**, tripling in velocity due to commercial proliferation.
- **The 82.8% Mass Transparency Gap:** While tracking 32,000+ objects, high-fidelity mass data is only available for ~17% of the catalog. This project utilized **Tier 1 Imputations** to reclaim 80% of this data, revealing the true kinetic energy of the "invisible" fleet.
- **The Kessler Canyon (Orbital Segregation):** KDE analysis reveals a distinct segregation of risk. While active satellites cluster in the "Commuter Lane" (~550km), massive abandoned rocket bodies form a permanent "Deadly Ring" at ~900km.

---

### **Visualizing the Crisis**

#### **1. The Great Kessler Acceleration (Initial Discovery)**

![Great Acceleration](images/great_acceleration.png)

_The first point of discovery using the UCS Satellite Database. This model identifies the precise decoupling point where active satellite deployment transitioned from a linear progression to an exponential arc._

#### **2. The Modern Sprint (Full Catalog Validation)**

![Modern Sprint](images/modern_sprint.png)

_Validation of the acceleration using the full 32,000+ object SATCAT registry. This visual confirms that the 2014 Pivot is not just an active-satellite trend, but an environment-wide shift affecting all orbital categories._

#### **3. The Mass Gap (Tier 1 Analysis)**

![Kessler Reality Check](images/kessler_reality_check.png)

_The "Reality Check" reveals the 82.8% Mass Gap. The **Red** area represents the massive amount of "Hidden" kinetic fuel identified through Tier 1 ESA proxy modeling._

#### **4. The Double Threat: Population vs. Kinetic Fuel**

![Double Threat](images/double_threat.png)

_A dual-axis synthesis of the crisis. While the **Population (Blue)** is exploding post-2014, the total **Kinetic Mass (Magenta)** continues its relentless climb, creating a pincer maneuver of orbital risk._

#### **5. The Kessler Canyon (The Traffic Map)**

![Kessler Traffic Map](images/kessler_traffic_map.png)

_Mapping the physical highways of risk. This Kernel Density Estimation (KDE) reveals the high-density **Commuter Lane (Lime)** sitting precariously beneath the high-mass **Deadly Ring (Red)** of legacy rocket bodies._

---

### **Scientific Methodology**

#### **1. UCS Pipeline: The Physics Reconstruction Engine**

To normalize the active satellite registry (`ucs_cleanup.ipynb`), we rejected the standard "Drop Nulls" approach which discards 40%+ of physics data. Instead, we built a tiered imputation engine:

- **The "White Whale" Exception:** Manually pinned the **ISS** mass (450,000 kg) to prevent it from skewing statistical baselines.
- **Grouped Median Imputation:** Imputed missing `Launch Mass` and `Power` using the median of satellites with similar **Orbit Class** and **Mission Purpose** (e.g., inferring a missing Starlink mass from other LEO Communications satellites).
- **Derived Dry Mass (Kinetic Potential):** Calculated the **Structural Mass Fraction** (Dry-to-Wet Ratio) for each orbit class to derive `Dry Mass` from `Launch Mass`. This ensures collision models account for solid hardware rather than expended fuel.
- **Sector & Mission Flagging:** Decomposed complex user strings into binary sector flags (`is_commercial`, `is_military`) and standardized 30+ raw mission types into 7 machine-readable categories.

#### **2. SATCAT Pipeline: Closing the Visibility Gap (Tier 1 Imputation)**

To address the 82.8% transparency gap in the debris catalog (`satcat_cleanup.ipynb`), we implement a **Synthetic Mass Fill** using conservative categorical averages derived from ESA debris reports. This allows us to model the "Kinetic Fuel" of objects that lack public metadata:

- **Rocket Bodies:** Assigned **2,000 kg** (Conservative average for upper stages like Centaur or Falcon 9).
- **Inactive Satellites:** Assigned **1,000 kg** (Historical average for legacy payloads).
- **Debris:** Assigned **0.1 kg** (Statistical baseline for trackable fragments >10cm).

#### **3. Temporal Modeling: The Kessler Engine**

Using `scipy.optimize`, we fitted historical growth data against both Linear and Exponential models. This mathematically validated the **2014 Pivot**, proving the environment has entered a self-accelerating phase.

---

### **Technical Note: Why Versioning Matters**

In orbital mechanics modeling, version consistency is critical. The curve_fit functions I used to identify the **2014 Pivot** rely on specific NumPy backends to calculate residuals accurately. Furthermore, the **Kessler Canyon** KDE plots utilize specific Seaborn bandwidth logic that can vary between versions. Using the provided venv ensures these exact findings can be recreated with mathematical precision.

### **Installation & Setup**

To ensure the analysis runs with the correct library versions, please use a virtual environment. This prevents dependency conflicts and ensures the mathematical models and visualizations render as intended.

1.  **Clone the repository and navigate to the project root.**
2.  **Create and Activate the Virtual Environment:**

    - Create: `python -m venv venv`
    - Activate (Windows Git Bash): `source venv/Scripts/activate`
    - Activate (Windows CMD): `.\venv\Scripts\activate`
    - Activate (Windows PowerShell): `.\venv\Scripts\Activate.ps1`
    - Activate (Mac/Linux): `source venv/bin/activate`

3.  **Install Project Dependencies:**

    - pip install -r requirements.txt

4.  **Data Verification:** Ensure raw data files are in data/original/ and cleaned outputs are directed to data/clean/.
5.  **Execution Order:**

    - **`ucs_cleanup.ipynb`**: Normalization & Physics Reconstruction (Active Satellites).
    - `ucs_eda.ipynb`: Initial Pivot Identification.
    - **`satcat_cleanup.ipynb`**: SATCAT Merge & Debris Proxying (Tier 1 Imputation).
    - `satcat_eda.ipynb`: Final Intelligence Briefing.

---

### **AI Attribution & Usage Disclosure**

In alignment with professional data science standards, I utilized the **Gemini 3** model family (**Flash & Pro**) as a technical thought partner and pair-programmer. Developing within **VS Code** and utilizing its integrated terminal and extensions, I targeted my usage of AI toward specific engineering and analytical goals:

- **Mathematical Prototyping:** I collaborated with **Gemini 3 Pro** to prototype the scipy.optimize curve-fitting logic and the RMSE statistical validation for the 2014 Pivot.
- **Data Engineering Audit:** I used **Gemini 3 Flash** to peer-review my **Physics Reconstruction Engine** and verify the accuracy of the grouped median imputation logic.
- **Technical Documentation:** I utilized AI to assist with text formatting for the intelligence briefings and to troubleshoot shell-specific environment activation commands (Git Bash vs. PowerShell).

**Note:** All analytical decisions, data filtering thresholds (The Kessler Canyon), and strategic findings (The Double Threat) are my original conclusions based on the processed data.

---

### **License**

This project is licensed under the MIT License.
