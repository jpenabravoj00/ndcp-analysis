# National Database of Childcare Prices (NDCP) Analysis
### Econometric Surveillance, Affordability Burden Modeling & Policy Intelligence (2008–2022)

[![Python Pipeline](https://img.shields.io/badge/Pipeline-Python_3.10+-3776AB.svg?logo=python&logoColor=white)](#-data-architecture--pipeline-methodology)
[![Interactive Report](https://img.shields.io/badge/Report-Interactive_HTML_Plotly-10B981.svg)](reports/ndcp_interactive_report.html)
[![Domain](https://img.shields.io/badge/Domain-Health_Economics_|_Public_Policy-blue.svg)](#-domain-background--author)
[![Data](https://img.shields.io/badge/Data-US_Department_of_Labor_NDCP-orange.svg)](#-data-architecture--pipeline-methodology)

---

## 📌 Executive Decision Brief

> **Primary Stakeholders**: State Child Care and Development Fund (CCDF/CCDBG) Administrators, State Workforce Development Boards, Municipal Family Policy Councils, and Corporate Benefits Strategists.
>
> **Core Problem**: Center-based infant childcare prices have escalated at more than double the rate of real wage growth, consuming up to **25%–35% of median household income** in metropolitan and suburban counties—far surpassing the US Department of Health and Human Services (HHS) **7% affordability threshold**. This dynamic triggers maternal labor force attrition, acute subsidy cliff effects, and severe regional workforce constraints.
>
> **Strategic Objective**: Provide decision-makers with an empirical, county-level econometric surveillance pipeline to **recalibrate sliding-scale copayments**, **target subsidy floors to true 75th-percentile market rates**, and **model geographic price friction indices across all 50 states**.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 EXECUTIVE KPI SNAPSHOT                                      │
├───────────────────────────────┬───────────────────────────────┬─────────────────────────────┤
│   +79.7% Price Escalation     │    25% - 35% Income Burden    │    r = 0.58 Price Elasticity│
│   $115.54/wk (2008)           │    Metropolitan County Rate   │    Strong responsiveness to │
│   → $207.60/wk (2022)         │    vs. 7% HHS Benchmark       │    local purchasing power   │
└───────────────────────────────┴───────────────────────────────┴─────────────────────────────┘
```

---

## 🎯 Actionable Policy & Operational Recommendations

Rather than treating childcare prices as a passive descriptive metric, this framework translates empirical findings into three high-impact decision levers:

| # | Empirical Finding | Operational / Policy Risk | Strategic Actionable Recommendation |
| :-: | :--- | :--- | :--- |
| **1** | **Longitudinal Acceleration (+79.7%)**:<br>Infant care surged from \$115.54 to \$207.60/week, compounding faster than consumer price indices. | Biennial state Market Rate Surveys (MRS) lag market shifts, causing providers to opt out of subsidized programs due to inadequate reimbursement. | **Annual Subsidy Floor Recalibration**: Transition from biennial to annual Market Rate Survey updates, mandating base subsidy reimbursement at or above the true regional 75th percentile. |
| **2** | **Extreme Affordability Burden (25%–35%)**:<br>Exceeds the federal 7% affordability cap by up to 500% in high-cost metro and suburban counties. | Sharp subsidy cliffs penalize working families earning 150%–200% FPL, driving involuntary maternal workforce exits. | **Graduated Sliding-Scale Copay Ceilings**: Enact local graduated copay subsidies capping out-of-pocket infant care costs at 7% of gross income for families between 150% and 250% FPL. |
| **3** | **Geographic Friction & Income Elasticity ($r=0.58$)**:<br>High-cost states average >\$250–\$350/week, while lower-cost regions sit at \$120–\$150/week. | Statewide flat reimbursement rates starve high-cost urban and suburban providers while misallocating rural resources. | **Tiered Regional Price Friction Adjustments**: Replace flat statewide rates with localized Price Friction Index multipliers tied to county-level housing and wage density. |

---

## 📊 Key Visualizations & Decision Insights

### 1. Longitudinal Price Growth Trajectory (2008–2022)
> National median weekly costs for infant center-based care surged from **\$115.54/week** in 2008 to **\$207.60/week** in 2022 (+79.7% growth), significantly outpacing real wage growth over the same period.

![National & Florida Infant Cost Trends](images/national_infant_cost_trends.png)

* **Decision Takeaway**: The steepening slope after 2014 underscores the failure of static subsidy allocations. Administrators must integrate automated inflation-adjustment mechanisms into multi-year budget appropriations.

---

### 2. State-Level Geographic Price Disparities
> Infant care costs exhibit extreme geographic variance across the United States. High-cost states (such as Washington D.C., Massachusetts, New York, and California) average well above \$250–\$350/week, whereas lower-cost southern and midwestern states sit near \$120–\$150/week against the national benchmark of \$161.4/week.

![Geographic Disparities in Weekly Infant Childcare Costs by State](images/state_cost_disparities.png)

* **Decision Takeaway**: Single statewide baseline rates create critical market failures in metropolitan hubs. Policy interventions must be calibrated using county-level variance indices rather than aggregate state averages.

---

### 3. Income Elasticity & Econometric Correlation
> Childcare costs scale positively with county-level median household income ($r = 0.58$), confirming strong price responsiveness to local purchasing power, while creating severe affordability bottlenecks in middle- and lower-income urban/suburban counties.

![County Median Household Income vs Weekly Infant Care Costs](images/income_vs_childcare_cost_correlation.png)

* **Decision Takeaway**: The variance band widens dramatically in counties above \$80,000 MHI. Regional economic developers should incentivize public-private employer childcare consortia to alleviate capacity constraints.

---

## 🌐 Interactive Data Intelligence Product

In addition to static publication figures, this repository includes an **executive-ready interactive HTML report** powered by Plotly:

* **File Location**: [`reports/ndcp_interactive_report.html`](reports/ndcp_interactive_report.html)
* **Core Capabilities**:
  * Hover tooltips displaying exact county-level income, weekly childcare price, and computed affordability ratios across 3,000+ US counties.
  * Multi-dimensional state and regional filtering with zoom and panning.
  * Executive KPI metric cards tracking overall growth and elasticity coefficients.
* **How to view**:
  * **Option 1 (Live Interactive Demo on GitHub Pages)**: [**Launch Live Report on GitHub Pages**](https://jpenabravoj00.github.io/ndcp-analysis/)
  * **Option 2 (Local Browser)**: Clone this repo and open `reports/ndcp_interactive_report.html` or `index.html` in any web browser.
  * **Option 3 (Interactive Jupyter Notebooks)**: Run notebooks locally for live cell execution and parameter exploration.

---

## 💡 Core Analytical & Econometric Metrics

### 1. Affordability Burden Ratio (ABR)
$$\text{Affordability Burden Ratio} = \frac{\text{Annualized Median Infant Care Price (Weekly Price} \times 52)}{\text{County Median Household Income (USD)}} \times 100$$
* **Friction Point**: Measures the proportion of gross household income required to sustain center-based infant care. In numerous metropolitan counties, this ratio exceeds **25%–35%**, far above the US Department of Health and Human Services (HHS) recommended affordability benchmark of **7%**.

### 2. Temporal Inflation Velocity (TIV)
$$\text{Price Inflation Velocity} = \frac{\text{Price}_t - \text{Price}_{t-1}}{\text{Price}_{t-1}} \times 100$$
* **Friction Point**: Tracks annual compounding growth rates in childcare prices across infant (`mcinfant`), toddler (`mctoddler`), and preschool (`mcpreschool`) cohorts to determine which care tiers exert the steepest financial strain.

### 3. Geographic Price Friction Index (PFI)
$$\text{Price Friction Index} = \frac{\text{State/County Median Care Price}}{\text{National Baseline Care Price}}$$
* **Friction Point**: Quantifies regional cost deviations relative to national baseline norms, highlighting jurisdictions requiring targeted childcare subsidy calibrations.

---

## ⚖️ Methodological Rigor & Explicit Analytical Trade-Offs

To maintain transparency and decision-grade reliability, key methodological choices and constraints were established:

1. **Center-Based (`mcinfant`) vs. Family Child Care (`fhinfant`) Selection**:
   * *Rationale*: Analysis prioritizes center-based infant care because it represents the largest single direct expense for working households and the most acute regulatory/capacity bottleneck in urban labor markets.
2. **Macroeconomic Baseline (`mhi_2022`) Selection**:
   * *Rationale*: Utilizes 2022 inflation-adjusted median household income (`mhi_2022`) from the US Census Bureau to standardize purchasing power across multi-year cohorts, mitigating distortion from short-term nominal wage fluctuations.
3. **Survey Imputation & State Participation Constraints**:
   * *Handling*: The NDCP dataset combines primary state Market Rate Surveys with DOL-imputed intermediate years. Imputation flags are explicitly tracked to prevent over-interpreting short-term post-2020 pandemic volatility.
   * *Geographic Notes*: Specific state survey non-participation (such as historical gaps in Florida market rate tables) are programmatically verified and isolated to prevent distortion of national aggregation baselines.
4. **County FIPS Integrity**:
   * *Handling*: FIPS codes are explicitly parsed and cast as 5-character zero-padded string identifiers (`dtype={'county_fips_code': str}`) to prevent spatial merge errors in GIS joins.

---

## 🛠️ Data Architecture & Pipeline Methodology

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Data Ingestion (ndcp_data_ingestion_notebook.py)              │
│ - Automated download of raw NDCP Excel dataset (US DOL)         │
│ - Raw staging to NDCP_2008-2022.xlsx                            │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. Data Cleaning & Normalization (ndcp_data_cleaning_notebook.py)│
│ - Standardizes column headers and geographic FIPS codes         │
│ - Handles missing data, imputation tags, and type coercions      │
│ - Exports clean baseline: ndcp_2008-2022_cleaned.csv            │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. Econometric Analysis (ncdp_data_analysis_notebook.py)        │
│ - Computes national averages, state rankings, and correlations  │
│ - Evaluates income vs. price elasticity and labor participation │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. Visualization & Reporting (generate_visuals.py)               │
│ - Generates high-resolution 300-DPI publication figures          │
│ - Builds interactive standalone Plotly HTML dashboard report    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```
ndcp-analysis/
├── .gitattributes                                 # Linguist overrides (vendors HTML, prioritizes Python)
├── README.md                                      # Executive Decision Brief & Master Documentation
├── requirements.txt                               # Python Dependencies
├── generate_visuals.py                            # Production Script: Generate Images & HTML Report
├── ndcp_data_ingestion_notebook.py                # Pipeline Step 1: Ingestion
├── ndcp_data_cleaning_notebook.py                 # Pipeline Step 2: Cleaning & FIPS Normalization
├── ncdp_data_analysis_notebook.py                 # Pipeline Step 3: Econometric Analysis
├── ncdp_data_visualization_notebook.py            # Pipeline Step 4: Exploratory Visualization
├── ndcp_data_cleaning_notebook.ipynb              # Executable Jupyter Notebook: Cleaning
├── ncdp_data_analysis_notebook.ipynb              # Executable Jupyter Notebook: Analysis
├── ncdp_data_visualization_notebook.ipynb         # Executable Jupyter Notebook: Visualization
├── ndcp_2008-2022_cleaned.csv                     # Cleaned Dataset (Analysis Ready)
├── images/
│   ├── national_infant_cost_trends.png            # High-Res Plot: Longitudinal Cost Trend
│   ├── state_cost_disparities.png                 # High-Res Plot: State Cost Rankings
│   └── income_vs_childcare_cost_correlation.png   # High-Res Plot: Econometric Scatter & Trend
└── reports/
    └── ndcp_interactive_report.html               # Standalone Interactive HTML Intelligence Report
```

---

## ⚡ How to Reproduce

### 1. Environment Setup
```bash
git clone https://github.com/jpenabravoj00/ndcp-analysis.git
cd ndcp-analysis
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Execute Data Pipeline
```bash
# 1. Ingest raw NDCP data from US DOL
python ndcp_data_ingestion_notebook.py

# 2. Clean data and generate standardized CSV
python ndcp_data_cleaning_notebook.py

# 3. Perform statistical & econometric analysis
python ncdp_data_analysis_notebook.py

# 4. Generate all visual artifacts and interactive HTML report
python generate_visuals.py
```

### 3. View the Interactive Report
Open `reports/ndcp_interactive_report.html` in any modern web browser.

---

## 👨‍🔬 Domain Background & Author

**Author**: **José I. Peña Bravo, PhD**  
*Neurophysiologist • Medical Educator • Healthcare & Policy Data Strategist*

* **PhD in Neuroscience** (Medical University of South Carolina): Investigated prefrontal cortex synaptic plasticity and neural circuit mechanisms underlying decision-making and behavior.
* **Former Healthcare Data Analyst & Interim Program Manager** (Florida Dept. of Health in Duval County – CDC Overdose Data to Action / OD2A Program): Directed public health surveillance pipelines, spatial analysis, and epidemiological metric modeling.
* **Applied Analytical Focus**: Transforming complex epidemiological, demographic, and socioeconomic datasets into actionable, decision-grade intelligence dashboards and reproducible computational pipelines.
* **Connect**: [LinkedIn](https://linkedin.com/in/josepenabravo) | [GitHub](https://github.com/jpenabravoj00)

---

## 📜 License & Acknowledgments

* **Data Source**: [US Department of Labor Women's Bureau - National Database of Childcare Prices (NDCP)](https://www.dol.gov/agencies/wb/topics/featured-childcare).
