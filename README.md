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

---

### Technical Highlights

- **Growth Modeling:** Applied mathematical best-fit curves to distinguish between linear launch rates and exponential debris accumulation.
- **Multi-Dataset Visualization:** Created comparative plots using UCS data to show the ratio of commercial vs. government payloads and their intended orbital classes.
- **Boolean Masking:** Isolated "unhealthy" tracking flags to identify which object categories pose the greatest risk to orbital situational awareness.
- **Data Merging:** Integrated disparate datasets via **NORAD IDs** to separate active infrastructure from historical clutter.
- **Categorical Proportions:** Utilized pie charts and grouped counts to visualize the dominance of dead payloads in the tracking catalog.

### Installation & Setup

1. Clone the repository.
2. Ensure data files are in `data/original/` and `data/clean/`.
3. **Execution Order:**
   - Run `ucs_cleanup.ipynb` (Standardizing UCS records)
   - Run `satcat_cleanup.ipynb` (Standardizing SATCAT/CelesTrak records)
   - Run `ucs_eda.ipynb` (Visualizing active satellite distribution and ownership)
   - Run `satcat_eda.ipynb` (Main Analysis: Debris, Growth, and Tracking Health)

---

### Data Sources

- **Union of Concerned Scientists (UCS):** In-depth records of active satellites (Owner, Purpose, Mass, Orbit).
- **CelesTrak (NORAD/SATCAT):** Historical catalog of all man-made objects ever launched and their current tracking statuses.

### License

This project is licensed under the MIT License.
