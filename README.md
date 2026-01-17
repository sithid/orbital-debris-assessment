# Orbital Clutter: Analyzing the Pollution of LEO

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### Project Description

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data from the **Union of Concerned Scientists (UCS)** with the **CelesTrak SATCAT**, this analysis quantifies the **Visibility Gap** and evaluates the environment against the **Kessler Syndrome**—the tipping point where orbital collisions become self-sustaining.

### Key Insights

- **The 50% Visibility Gap:** Nearly half of all objects with "unhealthy" tracking status (e.g., NEA - No Elements Available) are intact Inactive Satellites. These "Zombie Satellites" represent massive, unmonitored kinetic risks.
- **Evidence of Kessler Syndrome:** Analysis of LEO population trends shows a transition from linear growth to an exponential curve, punctuated by catastrophic fragmentation events in 2007 and 2009.

---

### Technical Highlights

- **Growth Modeling:** Applied mathematical best-fit curves to distinguish between linear launch rates and exponential debris accumulation.
- **Boolean Masking:** Isolated "unhealthy" tracking flags to identify which object categories pose the greatest risk to orbital situational awareness.
- **Data Merging:** Integrated disparate datasets via **NORAD IDs** to separate active infrastructure from historical clutter.
- **Categorical Proportions:** Utilized pie charts and grouped counts to visualize the dominance of dead payloads in the tracking catalog.

### Installation & Setup

1. Clone the repository.
2. Ensure data files are in `data/original/` and `data/clean/`.
3. **Execution Order:**
   - Run `ucs_cleanup.ipynb`
   - Run `satcat_cleanup.ipynb`
   - Run `ucs_eda.ipynb` (EDA/Analysis)
   - Run `satcat_eda.ipynb` (EDA/Analysis)

---

### Data Sources

- **Union of Concerned Scientists (UCS):** Active satellite records.
- **CelesTrak (NORAD/SATCAT):** Historical catalog and tracking statuses.

### License

This project is licensed under the MIT License.
