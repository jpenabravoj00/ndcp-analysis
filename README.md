# Analysis of the National Database of Childcare Prices (2008-2022)

## Project Description
This project analyzes the National Database of Childcare Prices (NDCP) to uncover trends in childcare costs across the United States from 2008 to 2022. A key focus of this analysis is comparing national and state-level data against the specific trends and data points for the State of Florida. It reveals significant cost increases over time, stark geographic disparities between states, and a notable correlation between local income levels and childcare prices. The project is structured as a series of Jupyter Notebooks (run as Python scripts) that cover data ingestion, cleaning, analysis, and visualization.

## Programming Languages & Libraries Used
- **Programming Language:** Python
- **Core Libraries:**
  - `pandas` for data manipulation and analysis
  - `matplotlib` and `seaborn` for data visualization
  - `requests` for programmatic data download
  - `openpyxl` for reading Excel files

## Project Objective
The primary objective is to move from the raw NDCP dataset to actionable insights suitable for a data portfolio. This involves:
- Establishing a reproducible workflow for data acquisition and cleaning
- Analyzing national and state-level trends in childcare costs over time, using Florida as a key benchmark for comparison
- Investigating the relationship between childcare prices and local economic factors, such as household income
- Creating a series of clear and compelling visualizations to communicate the findings

## Dataset
- **Source:** National Database of Childcare Prices (NDCP)
- **URL:** [https://www.dol.gov/sites/dolgov/files/WB/NDCP2022.xlsx](https://www.dol.gov/sites/dolgov/files/WB/NDCP2022.xlsx)
- **Description:** County-level data on median childcare prices by provider type and child’s age, along with various demographic and economic indicators for the years 2008 through 2022.

## How to Run This Project

The project is broken down into a series of scripts that should be run in the following order. It is recommended to use a virtual environment.

1. **ndcp_data_ingestion.py**: Downloads the raw `.xlsx` file from the source URL and saves it locally.
2. **ndcp_data_cleaning.py**: Loads the raw data, standardizes column names, handles missing values and duplicates, and saves a cleaned version as `ndcp_2008-2022_cleaned.csv`.
3. **ndcp_data_analysis.py**: Loads the cleaned data and performs the core analysis, calculating national trends, state-level comparisons, and economic correlations.
4. **ndcp_data_visualization.py**: Generates the key plots (line chart, bar chart, scatter plot) based on the analysis.

## Key Analytical Questions Explored
- How do childcare cost trends in Florida compare to the national average between 2008 and 2022?
- Where does Florida rank in terms of average childcare costs compared to other states?
- Is the correlation between county-level income and childcare prices different in Florida compared to the rest of the nation?

## Known Limitations
- **Data Imputation and Gaps:** The dataset relies on significant imputation to fill gaps between market rate surveys (e.g., Florida’s 2008 data was imputed based on 2007 figures; a total of 13 years of data for the state involved some level of imputation).
- **Complex Aggregation (Florida):** For certain years (e.g., 2013 and 2015), Florida’s county-level rates are an aggregated, weighted average of different provider types ("gold seal" and "non-gold seal"), which may not be directly comparable to other states with simpler reporting.
- **Specific Data Exclusions:** The analysis excludes certain provider types, such as "Large Family Child Care Homes" in Florida, which could affect the overall cost representation.
- **Missing Recent Data:** For the 2021-2022 period, price data for several Florida counties was missing at the 50th and 75th percentile, impacting the completeness of the most recent trends.