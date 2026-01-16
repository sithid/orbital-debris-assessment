# Orbital Clutter: Analyzing the Pollution of LEO

### Project Description

This project investigates the growing crisis of space debris and satellite congestion in Low Earth Orbit (LEO). By merging active satellite data from the **Union of Concerned Scientists (UCS)** with the **CelesTrak SATCAT** (Satellite Catalog), this analysis identifies key historical events—such as the **March 2000 Long March 4B breakup**—that transformed space from a "wilderness" into a high-risk environment.

The goal is to demonstrate that while "New Space" (commercial) is driving current growth, "Old Space" (early missions) left behind a legacy of debris that threatens modern infrastructure.

### Installation & Setup

To run this analysis locally, you will need **Python 3.x** and the following libraries:

- `pandas` – For data manipulation and merging.
- `matplotlib` & `seaborn` – For generating visualizations.
- `scipy` – Used for calculating linear vs. exponential growth models.

**Setup Steps:**

1. Clone this repository.
2. Ensure your data folder structure is as follows:
   - `data/original/satcat.csv`
   - `data/clean/ucs_cleaned.csv`
3. Install the necessary dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Run `satcat_cleanup.ipynb` first to generate the master clutter dataset.
5. Run `satcat_eda.ipynb` to view the visualizations.

### Usage Examples

The project includes several key visualization patterns:

- **The "Smoking Gun" Bar Chart:** Highlights the massive spikes in debris additions during 2000, 2007, and 2009.
- **Linear vs. Exponential Growth:** A specific look at LEO congestion using mathematical best-fit curves.
- **Orbit Composition:** A stacked bar chart showing the ratio of active satellites to "junk" in various altitudes.

### Technical Highlights

- **Boolean Masking:** Used to isolate specific altitude zones (e.g., 250km - 500km) for detailed congestion analysis.
- **Pivot Tables:** Used to transform raw satellite lists into time-series data for growth modeling.
- **Data Merging:** Integrated the UCS and SATCAT datasets using **NORAD IDs** to distinguish between active payloads and inactive debris.

### Credits & Contributors

- **Lead Analyst:** [Your Name]
- **Course:** Data Analysis Pathway with **Code:You**.
- **Data Sources:** Union of Concerned Scientists (UCS) and CelesTrak (NORAD/SATCAT).

### License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code for educational purposes.

---

### Notes
This project is still very much under development and is subject to change in various ways at any time.  This readme will be updated and evolve as the project does.