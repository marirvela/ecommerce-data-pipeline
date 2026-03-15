# E-commerce Data Pipeline andd Executive Analytics (2026 Project)

*[🇪🇸 Leer versión en Español](README-es.md)*

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

This project showcases a complete end-to-end data analytics ecosystem. It covers everything from raw transactional data extraction and cleaning using **Python ETL pipelines**, to the design of a high-impact **Executive Dashboard** in Power BI (featuring a modern Dark Mode / FinTech UI) built for strategic decision-making.

## Business Impact & KPIs
The analysis of the e-commerce database revealed the following key performance indicators:
* **Total Sales:** $113 Million USD generated.
* **Return on Investment (ROI):** Reached a massive **915.86%**, demonstrating extraordinary efficiency in digital advertising spend ($11 Mill. Ad Spend).
* **Top Market:** The Federal Democratic Republic leads global sales, closely followed by Bolivia and Argentina.

## 📸 Executive Dashboard Preview
*(Interactive visualization developed in Power BI)*

![Dashboard Preview](images/final_dashboard.png)

## Technical Architecture & ETL Process
The project is structured to ensure reproducibility and clean data modeling:
* **`scripts/`**: Contains Python scripts (`etl_process.py`, `generate_data.py`) responsible for data generation, handling missing values, standardizing dates/currencies, and exporting the final clean tables.
* **`data/raw/`**: Original data sources (SQLite databases and Excel files).
* **`data/processed/`**: Cleaned and transformed CSV files ready for Data Modeling.
* **`dashboards/`**: Source Power BI report file (`.pbix`).

> **[Click here to read the full Executive Summary & Strategic Recommendations](EXECUTIVE_SUMMARY.md)**

---
**Data Engineering & Visualization by Mariana Rodriguez Velandia**