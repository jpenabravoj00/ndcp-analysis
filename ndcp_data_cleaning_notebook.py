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
# # Phase 3: Initial Data Exploration, Cleaning, and Pre-processing
#
# **Objective:** To assess the quality of the raw data, handle inconsistencies, and prepare a clean, analysis-ready dataset.

# %% [markdown]
# ### Notebook Setup: Load the Raw Data
#
# Before we can begin cleaning, we must load the raw data file (`NDCP_2008-2022.xlsx`) that was downloaded during Phase 2. This cell reads the Excel file into a pandas DataFrame named `ndcp_df`.

# %%
import pandas as pd

# Define the filename of the raw data downloaded in the previous step.
raw_data_filename = "NDCP_2008-2022.xlsx"

try:
    # Load the raw Excel data into the ndcp_df DataFrame.
    ndcp_df = pd.read_excel(raw_data_filename, engine='openpyxl')
    print(f"Successfully loaded '{raw_data_filename}'.")
    print(f"DataFrame created with {ndcp_df.shape[0]} rows and {ndcp_df.shape[1]} columns.")
except FileNotFoundError:
    print(f"ERROR: The file '{raw_data_filename}' was not found.")
    print("Please make sure you have run the 'ndcp_data_ingestion.py' script first to download the data.")
except Exception as e:
    print(f"An error occurred while loading the file: {e}")


# %% [markdown]
# ### Step 1: Standardize Column Names
#
# To prevent `KeyError` issues from typos, capitalization, or special characters, we will standardize all column names to a consistent `snake_case` format. This involves converting them to lowercase and replacing spaces or periods with underscores.

# %%
# Store original columns for comparison.
original_columns = ndcp_df.columns.tolist()

# Standardize column names.
ndcp_df.columns = ndcp_df.columns.str.lower().str.replace(' ', '_').str.replace('.', '', regex=False)

# Store new columns and print a summary of changes.
new_columns = ndcp_df.columns.tolist()
print("--- Column Name Standardization Complete ---")

# Create a dictionary to show which columns were renamed.
column_changes = {old: new for old, new in zip(original_columns, new_columns) if old != new}

if column_changes:
    print("The following columns were renamed:")
    for old, new in column_changes.items():
        print(f"'{old}'  --->  '{new}'")
else:
    print("All column names were already in the correct format.")


# %% [markdown]
# ### Step 2: Column and Data Type Verification
#
# Now that column names are standardized, we'll verify the data types (`dtypes`). This helps confirm that pandas has interpreted the data as expected.

# %%
# First, let's re-verify the columns and their data types.
# This cell should now run without errors.
print("\n--- Column Data Types ---")
print(ndcp_df.dtypes)

# %% [markdown]
# **Observation:** According to the data dictionary (`2025-08-18_Childcare_Data_Proj`), the `county_fips_code` should be treated as a string to preserve leading zeros, which are significant for identification. We will correct this.

# %% [markdown]
# ### Step 3: Data Type Correction
#
# Based on our observation, we need to convert the `county_fips_code` to a string type. A standard FIPS code should be 5 digits long, so we will pad any shorter codes with a leading zero.

# %%
# Convert 'county_fips_code' to a string data type.
# We first fill any potential missing values with '0' before conversion.
ndcp_df['county_fips_code'] = ndcp_df['county_fips_code'].fillna(0).astype(int).astype(str)

# Pad the string with leading zeros to ensure a consistent 5-digit length.
ndcp_df['county_fips_code'] = ndcp_df['county_fips_code'].str.zfill(5)

# Verify the change by checking the first few values and the new data type.
print("--- Corrected 'county_fips_code' ---")
print(ndcp_df['county_fips_code'].head())
print("\nNew Dtype:", ndcp_df['county_fips_code'].dtype)

# %% [markdown]
# ### Step 4: Identify and Quantify Missing Values
#
# Missing data can significantly impact analysis. We need to identify which columns contain missing values (`NaN`) and determine the extent of the problem.

# %%
# Calculate the total number of missing values for each column.
missing_values = ndcp_df.isnull().sum()

# Calculate the percentage of missing values for each column.
missing_percentage = (missing_values / len(ndcp_df)) * 100

# Create a summary DataFrame to display the results clearly.
missing_summary = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage (%)': missing_percentage
})

# Display the summary, focusing on columns that have missing data.
print("--- Missing Data Summary ---")
print(missing_summary[missing_summary['Missing Values'] > 0].sort_values(by='Percentage (%)', ascending=False))

# %% [markdown]
# ### Step 5: Develop a Strategy for Missing Values
#
# **Observation:** A significant number of rows are missing data for the core childcare price variables (e.g., `mc_infant`, `mfcc_infant`).
#
# **Strategy:**
# - For our primary analysis on childcare prices, we cannot use rows where price data is missing.
# - Instead of dropping these rows globally, which could remove valuable demographic data for other types of analysis, we will filter the DataFrame as needed for specific tasks. This approach preserves the maximum amount of information.

# %%
# Let's identify the key price-related columns.
price_columns = [
    'mcsa', 'mfccsa', 'mcinfant', 'mctoddler', 'mcpreschool',
    'mfccinfant', 'mfcctoddler', 'mfccpreschool'
]

# Calculate how many rows have at least one missing value in these critical price columns.
rows_with_missing_prices = ndcp_df[price_columns].isnull().any(axis=1).sum()
total_rows = len(ndcp_df)

print(f"Total rows in the dataset: {total_rows}")
print(f"Rows with at least one missing price value: {rows_with_missing_prices}")
print(f"Percentage of rows with missing prices: {(rows_with_missing_prices / total_rows) * 100:.2f}%")
print("\nNote: We will filter these rows out during price-specific analysis.")


# %% [markdown]
# ### Step 6: Identify and Handle Duplicate Rows
#
# Duplicate rows can skew results and should be removed. We will check for and eliminate any complete duplicates.

# %%
# Check for the number of fully duplicate rows in the dataset.
duplicate_rows = ndcp_df.duplicated().sum()
print(f"Found {duplicate_rows} duplicate rows.")

# If duplicates are found, remove them.
if duplicate_rows > 0:
    ndcp_df = ndcp_df.drop_duplicates()
    print("Duplicate rows have been removed.")
    # Verify removal
    print(f"Remaining duplicate rows: {ndcp_df.duplicated().sum()}")


# %% [markdown]
# ### Step 7: Outlier Detection with Descriptive Statistics
#
# A powerful initial step for outlier detection is to generate summary statistics for all numerical columns. This allows us to check for logical impossibilities (e.g., negative prices, percentages over 100) by examining the `min` and `max` values.

# %%
# Generate descriptive statistics for all numerical columns.
# Using .T transposes the output for easier reading.
print("--- Descriptive Statistics for Numerical Columns ---")
print(ndcp_df.describe().T)

# %% [markdown]
# **Action:** Review the `min` and `max` columns in the table above. Pay close attention to price columns (e.g., `mc_infant`), rates (e.g., `unr_16`), and percentages to ensure they fall within logical ranges. At a glance, the values appear to be within reasonable bounds, but a more detailed investigation could be performed for specific columns if anomalies were detected.

# %% [markdown]
# ### Step 8: Save the Cleaned Data
#
# To conclude the pre-processing phase, we will save our cleaned and prepared DataFrame to a new file. This is a crucial best practice, as it creates a checkpoint and separates our cleaning logic from the upcoming analysis phase. We will use the CSV format for its compatibility.

# %%
# Define the filename for the cleaned data.
cleaned_filename = "ndcp_2008-2022_cleaned.csv"

try:
    # Save the cleaned DataFrame to a CSV file.
    # index=False prevents pandas from writing row indices into the file.
    ndcp_df.to_csv(cleaned_filename, index=False)
    print(f"Cleaned data successfully saved as '{cleaned_filename}'.")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")
# %%
