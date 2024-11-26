import os
import site
import sys

import pandas as pd
import requests

print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Site packages:", site.getsitepackages())

# URL of the Palmer Penguins dataset CSV
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"

# Specify the folder to save the dataset
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)
csv_path = os.path.join(data_folder, "penguins.csv")

try:
    # Download the dataset
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Save the dataset to a CSV file
    with open(csv_path, "wb") as file:
        file.write(response.content)

    # Load the dataset into a pandas DataFrame
    penguins = pd.read_csv(csv_path)

    # Display the first few rows of the dataset
    print("Dataset successfully downloaded and saved.")
    print(penguins.head())

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
