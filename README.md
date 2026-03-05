# COVID-19 Global Dashboard

An end-to-end data analytics project exploring global COVID-19 trends, mortality rates, and vaccination impact using Python, Azure SQL Database, and Power BI.

---

## Project Overview

This project analyzes the Our World in Data COVID-19 dataset to uncover meaningful public health insights, including the relationship between vaccination rates and mortality, regional trends, and year-over-year comparisons. The dashboard is designed to support data-driven decision-making through interactive visualizations.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas, SQLAlchemy) | Data cleaning and ingestion |
| Azure SQL | Data storage and SQL querying |
| Power BI | Dashboard and visualization |
| Git | Version control |

---

## Data Source

Our World in Data — COVID-19 Dataset  
https://ourworldindata.org/covid-deaths

The dataset covers global COVID-19 cases, deaths, and vaccination records from January 2020 onwards.

---

## Data Pipeline

```
Raw CSV → import.py → MySQL → Azureconnect.py → Azure SQL Database → Power BI Dashboard
```

1. **import.py**: Selected relevant columns, handled null values, converted date formats, and loaded data into local MySQL via SQLAlchemy
2. **Azureconnect.py**: Migrated cleaned data from local MySQL to Azure SQL Database on cloud using ActiveDirectory authentication
3. **Power BI**: Connected directly to Azure SQL Database, built date table, defined DAX measures, and developed three dashboard pages

---

## Dashboard Pages

### Page 1: Global Overview
- KPI cards: Total Cases, Total Deaths, Death Rate %, Avg Vaccination Rate
- Filled map showing case distribution by country
- Time range slicer for dynamic filtering

### Page 2: Trend Analysis
- 7-day average new cases line chart by continent
- Monthly new cases stacked bar chart
- Year-over-year growth comparison

### Page 3: Vaccination Impact
- Scatter plot: vaccination rate vs death rate by country
- Death rate trend before and after vaccine rollout (Dec 2020)
- Country vaccination rate ranking bar chart
- Pre/post vaccine average death rate KPI cards

---

## Key Insights

1. **Vaccination and mortality**: Countries with higher vaccination rates showed a notable decline in death rates from mid-2021 onwards, particularly in Europe and North America
2. **Regional disparity**: Africa and parts of Asia maintained lower reported case counts but faced delayed vaccine access, with vaccination rates remaining below 30% through 2021
3. **Wave patterns**: Clear seasonal wave patterns are visible across all continents, with major surges in late 2020, early 2021, and late 2021 (Omicron)
4. **Year-over-year trend**: Global new cases peaked in early 2022 before declining significantly, coinciding with widespread booster rollouts

---

## Project Structure

```
covid19-dashboard/
├── import.py              # Stage 1: CSV cleaning and ingestion into MySQL
├── Azureconnect.py        # Stage 2: Migration from MySQL to Azure SQL Database
├── README.md              # Project documentation
└── covid_dashboard.pbix   # Power BI dashboard file
```

---

## How to Run

1. Download the dataset from https://ourworldindata.org/covid-deaths
2. Update MySQL credentials in `import.py` and run to load data into local MySQL
3. Update Azure SQL credentials in `Azureconnect.py` and run to migrate data to Azure SQL Database
4. Open `covid_dashboard.pbix` in Power BI Desktop
5. Update Azure SQL connection settings to your own instance
6. Refresh data

---

## Author

Chelsea  
MSc Epidemiology & Health Statistics | MSc Data Science  
[GitHub](https://github.com/Chelsea616)
