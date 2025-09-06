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
# # Phase 2: Data Acquisition and Ingestion
#
# **Objective:** Programmatically download the National Database of Childcare Prices (NDCP) `.xlsx` data file from the specified URL and load it into a pandas DataFrame for analysis.

# %% [markdown]
# ### Step 1: Import Necessary Libraries
#
# We'll start by importing the essential Python libraries for this task.
# - `requests`: To handle the HTTP request for downloading the file from the web.
# - `pandas`: The core library for data manipulation and analysis in Python. It will be used to load the Excel file into a DataFrame.
# - `os`: To interact with the operating system, specifically to check if the data file already exists in our local directory. This prevents re-downloading the file every time the script is run.

# %%
import requests
import pandas as pd
import os

# %% [markdown]
# ### Step 2: Define URL and Local File Path
#
# We define the source URL and the desired local filename as variables. This is a best practice that makes the code cleaner and easier to update if the source URL or desired filename changes in the future.

# %%
# The direct URL to the raw .xlsx file.
url = "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022.xlsx"

# The name for the file once it's saved locally in our project directory.
local_filename = "NDCP_2008-2022.xlsx"

# %% [markdown]
# ### Step 3: Download the Data File
#
# This code block checks if the data file already exists locally. If it does not, it will download the file from the specified URL. This saves time and bandwidth by avoiding unnecessary downloads on subsequent runs.

# %%
# Check if the file already exists in the current directory.
if not os.path.exists(local_filename):
    print(f"File '{local_filename}' not found. Downloading from source...")
    try:
        # Send a GET request to the URL.
        response = requests.get(url, allow_redirects=True)
        
        # Raise an exception if the request was unsuccessful (e.g., 404 Not Found).
        response.raise_for_status()
        
        # Open the local file in write-binary mode and save the content.
        with open(local_filename, 'wb') as f:
            f.write(response.content)
            
        print(f"Successfully downloaded and saved as '{local_filename}'.")
        
    except requests.exceptions.RequestException as e:
        # Handle potential network errors or issues with the URL.
        print(f"An error occurred during download: {e}")
else:
    print(f"File '{local_filename}' already exists. Skipping download.")


# %% [markdown]
# ### Step 4: Load Data into a Pandas DataFrame
#
# Now that the file is available locally, we will load it into a pandas DataFrame. A DataFrame is a two-dimensional labeled data structure, similar to a spreadsheet, that will be the primary object for our analysis.

# %%
try:
    # Use pandas' read_excel function to load the data.
    # The 'openpyxl' engine is required for .xlsx files.
    ndcp_df = pd.read_excel(local_filename, engine='openpyxl')
    
    print("Data successfully loaded into a pandas DataFrame.")

except FileNotFoundError:
    print(f"Error: The file '{local_filename}' was not found. Please ensure it was downloaded correctly.")
except Exception as e:
    print(f"An error occurred while loading the Excel file: {e}")


# %% [markdown]
# ### Step 5: Initial Data Verification
#
# It is crucial to perform a quick, high-level verification of the data to ensure it has been loaded correctly. We will check its structure, size, and the data types of its columns.

# %%
# Check if the DataFrame was created before trying to use it.
if 'ndcp_df' in locals():
    # Display the first 5 rows to get a feel for the data.
    print("\n--- First 5 Rows of the DataFrame ---")
    print(ndcp_df.head())

    # Display the dimensions of the DataFrame (rows, columns).
    print("\n--- DataFrame Shape ---")
    print(f"The DataFrame has {ndcp_df.shape[0]} rows and {ndcp_df.shape[1]} columns.")

    # Display a concise summary, including data types and non-null values.
    # This is excellent for spotting initial data quality issues.
    print("\n--- DataFrame Info ---")
    ndcp_df.info()


# %%
