# Energy Data Quality & Intelligence Platform

* **[View Top 10 Country Quality Scores (Interactive HTML)](outputs/top_10_country_quality_scores.html)** *(Download or view locally to interact with the chart)*

An enterprise-grade data engineering, governance, and analytics platform designed to ingest, clean, validate, and score energy infrastructure statistics across African markets.

---

## Project Description
Energy planning and policy formulation across African nations frequently suffer from data fragmentation, delayed reporting cycles, and metadata inconsistencies. The Africa Energy Data Quality & Intelligence Platform acts as an automated data quality control tower. It transforms raw, multi-source repositories into a unified, clean, and rigorously audited data asset accompanied by exploratory notebooks, interactive visual assets, and composite usability scorecards.

---

## The Problem
* **Data Discrepancies & Anomalies:** Raw energy archives often contain reporting errors, such as negative electricity generation values or structural formatting gaps.
* **Missing Governance Metrics:** Analysts lack a quantitative benchmark to assess whether a given country's reported energy data is complete, current, and reliable.
* **Fragmented Formats:** Datasets from international repositories vary in schema (wide vs. long formats), making integration and multi-source analysis difficult.

---

## The Solution
This project implements a modular, sequential data pipeline spanning discovery, testing, automated validation, and intelligence:
1. **Data Discovery:** Profiles raw multi-source datasets, evaluates initial structures, and maps reporting anomalies.
2. **Cleaning & Transformation Tests:** Harmonizes repositories, resolves wide-to-long structures, and isolates structural anomalies (e.g., catching and resolving negative generation records).
3. **Automated Governance:** Runs automated schema integrity checks, missingness threshold evaluations, and boundary rules, exporting structured audit logs.
4. **Data Usability Scoring:** Computes a composite Data Quality & Usability Score (0–100) for every nation based on reporting recency, generation completeness, and capacity coverage.
5. **Interactive Intelligence:** Generates high-fidelity Plotly visual assets (continental trends and technology mixes) exported directly for reporting.

---

## Tech Stack
* **Language:** Python
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Data Governance & Validation:** Custom Python validation scripts & audit logging frameworks
* **Interactive Visualization & EDA:** Plotly, Jupyter Notebooks

---

## Data Sources
* **Ember:** Yearly electricity generation and capacity metrics by technology source.
* **IRENASTAT:** Renewable energy capacity statistics.
* **World Bank:** Macroeconomic and electrification development indicators.

---

## Results & Recommendations

### Key Findings from Data Audits
* **Data Usability Hierarchy:** Nations with robust reporting infrastructure (such as South Africa, Morocco, Rwanda, and Egypt) achieved composite usability scores above 97/100, driven by 100% generation completeness and recent reporting milestones.
* **Missingness Isolation:** Automated validation logs successfully flagged and managed metadata gaps while confirming 100% integrity across core identifier and generation fields.

### Strategic Recommendations
1. **Standardize Regional Reporting Templates:** Regional energy bodies should adopt automated validation rules during ingestion to catch anomalies (like negative generation entries) upstream.
2. **Improve Capacity Coverage Tracking:** While generation completeness is high across most major markets, expanding capacity data tracking in secondary grids will close remaining metadata gaps.

---

## Project Structure
```text
african-energy-data-platform/
│
├── data/
│   ├── raw/                        
│   └── processed/                  
│
├── notebooks/
│   ├── 01_data_discovery.ipynb     
│   ├── 02_cleaning_tests.ipynb     
│   └── 03_interactive_dashboard.ipynb 
│
├── outputs/
│   ├── quality_checks.csv          
│   ├── country_rankings.csv        
│   └── *.html                      
│
├── src/
│   ├── validate.py                 
│   └── quality_score.py            
│
└── README.md
└── requirements.txt
