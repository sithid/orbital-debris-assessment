# Orbital Clutter: Analyzing the Pollution of LEO

**Lead Analyst:** James Glosser  
**Course:** Data Analysis Pathway with **Code:You**

---

### Project Description

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data from the **Union of Concerned Scientists (UCS)** with the **CelesTrak SATCAT**, this analysis identifies historical "smoking gun" events and quantifies the **Visibility Gap**—the population of large, inactive objects that sensors struggle to track consistently.

The goal is to demonstrate that while "New Space" (commercial) is driving current growth, a legacy of "Old Space" debris and untrackable "Zombie Satellites" poses an immediate threat to modern infrastructure.

### Key Discovery: The Visibility Gap

A major finding of this EDA is that **Inactive Satellites alone account for nearly 50% of all objects with unhealthy tracking status codes** (e.g., NEA - No Elements Available). This proves that orbital risk is driven not just by small debris fragments, but by large, dead payloads that have become untrackable over time.

---

### Installation & Setup

To run this analysis locally, you will need **Python 3.x** and the following libraries:

- `pandas` – Data manipulation and Boolean masking.
- `matplotlib` & `seaborn` – Data visualization.
- `scipy` – Growth modeling.

**Execution Order:**

1. Run `ucs_cleanup.ipynb` and `satcat_cleanup.ipynb` to generate the master dataset.
2. Run `ucs_eda.ipynb` to generate analysis and visualizations of the ucs dataset.
3. Run `satcat_eda.ipynb` to generate the analysis and visualizations for the satcat dataset.

---

### Technical Highlights

- **Boolean Masking & Data Integrity:** Used to isolate "unhealthy" tracking flags (NEA, NCE, NIE) and determine their impact on data reliability.
- **Pivot Tables:** Transformed raw satellite lists into time-series data to compare linear vs. exponential growth models.
- **Data Merging:** Successfully integrated two disparate datasets using **NORAD IDs** to distinguish between active payloads and inactive clutter.
- **Categorical Proportions:** Utilized `value_counts` and pie charts to visualize the distribution of orbital anomalies across different object types.

### Usage Examples (Key Visualizations)

- **The "Smoking Gun" Timeline:** Bar charts highlighting massive debris spikes in 2000, 2007, and 2009.
- **Tracking Status Distribution:** A proportional analysis proving the dominance of Inactive Satellites in tracking failures.
- **Orbit Composition:** A stacked bar chart showing the ratio of active satellites to "junk" at various altitudes.

---

### Data Sources

- **Union of Concerned Scientists (UCS):** Active satellite database.
- **CelesTrak (NORAD/SATCAT):** Historical satellite catalog and tracking status.

### License

This project is licensed under the MIT License.
