# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Phase 4: Identifying Key Insights for a Data Portfolio Project
#
# **Objective:** To formulate and answer key analytical questions that reveal meaningful trends, relationships, and patterns within the childcare data.

# %% [markdown]
# ### Notebook Setup: Load the Cleaned Data
#
# Our first step is to load the `ndcp_2008-2022_cleaned.csv` file created in the previous phase. This ensures our analysis is performed on a clean, reliable dataset.

# %%
import pandas as pd
import numpy as np

# Define the filename of the cleaned data.
cleaned_data_filename = "ndcp_2008-2022_cleaned.csv"

try:
    # Load the cleaned CSV data into the ndcp_df DataFrame.
    # We specify dtype for 'county_fips_code' to ensure it's read as a string.
    df = pd.read_csv(cleaned_data_filename, dtype={'county_fips_code': str})
    print(f"Successfully loaded '{cleaned_data_filename}'.")
    print(f"DataFrame ready for analysis with {df.shape[0]} rows and {df.shape[1]} columns.")
except FileNotFoundError:
    print(f"ERROR: The file '{cleaned_data_filename}' was not found.")
    print("Please make sure you have run the 'ndcp_data_cleaning.py' script first to create the file.")
except Exception as e:
    print(f"An error occurred while loading the file: {e}")


# %% [markdown]
# ### Insight 1: Analyzing National Temporal Trends
#
# How have childcare costs changed over time at a national level? We will focus on a key metric: the median weekly price for center-based care for an infant (`mc_infant`), as this often represents one of the highest costs for families.

# %%
# First, create a new DataFrame that drops rows where 'mc_infant' is missing.
# This ensures our average is not skewed by missing data.
price_trends_df = df.dropna(subset=['mcinfant'])

# Group by 'study_year' and calculate the national average 'mc_infant' price.
# We use .mean() to get the average price for each year.
national_avg_price_by_year = price_trends_df.groupby('studyyear')['mcinfant'].mean().reset_index()

# Rename the columns for clarity.
national_avg_price_by_year.rename(columns={'mcinfant': 'national_average_infant_price'}, inplace=True)

print("--- National Average Weekly Price for Infant Center-Based Care ---")
print(national_avg_price_by_year)


# %% [markdown]
# ### Insight 2: Conducting a Geographic Comparison
#
# Where is childcare most and least expensive in the United States? We will group the data by state to identify the states with the highest and lowest average costs for infant care across the entire study period.

# %%
# Use the same 'price_trends_df' from the previous step.
# Group by 'state_name' and calculate the average 'mc_infant' price.
avg_price_by_state = price_trends_df.groupby('state_name')['mcinfant'].mean().sort_values(ascending=False).reset_index()

# Rename the columns for clarity.
avg_price_by_state.rename(columns={'mcinfant': 'average_infant_price'}, inplace=True)

# Identify the top 5 most expensive states.
top_5_expensive = avg_price_by_state.head(5)

# Identify the bottom 5 least expensive states.
bottom_5_expensive = avg_price_by_state.tail(5)

print("--- Top 5 Most Expensive States for Infant Care (Weekly Avg) ---")
print(top_5_expensive)
print("\n" + "="*60 + "\n")
print("--- Top 5 Least Expensive States for Infant Care (Weekly Avg) ---")
print(bottom_5_expensive)

# %% [markdown]
# ### Addressing the Florida Data Limitation
#
# As noted in our project plan, we suspect data for Florida is missing. It is critical to programmatically confirm this and explicitly state this limitation.

# %%
# Check if 'Florida' exists within the 'state_name' column.
is_florida_present = 'Florida' in df['state_name'].unique()

if not is_florida_present:
    print("CONFIRMATION: Data for the state of Florida is not present in this dataset.")
    print("All national averages and state-level comparisons will exclude Florida.")
else:
    print("Data for Florida was found in the dataset.")


# %% [markdown]
# ### Insight 3: Exploring Economic Correlations
#
# What is the relationship between childcare prices and key economic indicators in a county? We will investigate two important questions:
# 1.  Do counties with higher household incomes also have higher childcare costs?
# 2.  Is there a link between the rate of working mothers and childcare costs?

# %%
# Create a focused DataFrame for correlation analysis, dropping rows with missing values
# in any of the columns of interest to ensure accurate calculations.
correlation_df = df[['mcinfant', 'mhi_2022', 'flfpr_20to64_under6']].dropna()

# Calculate the correlation between infant care price and median household income.
price_income_corr = correlation_df['mcinfant'].corr(correlation_df['mhi_2022'])

# Calculate the correlation between infant care price and female labor force participation.
price_labor_corr = correlation_df['mcinfant'].corr(correlation_df['flfpr_20to64_under6'])

print("--- Correlation Analysis ---")
print(f"Correlation between Infant Care Price and Median Household Income: {price_income_corr:.4f}")
print(f"Correlation between Infant Care Price and Female Labor Force Participation (mothers with children < 6): {price_labor_corr:.4f}")

print("\n--- Interpretation ---")
print("A correlation coefficient near 1 indicates a strong positive relationship, near -1 indicates a strong negative relationship, and near 0 indicates a weak relationship.")


