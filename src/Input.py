# %% Imports
import pandas as pd

# %% Input Data
# A function that reads the input data from a csv

# RI, Na, Mg, Al, Si, K, Ca, Ba, Fe

input_folder = "../input/"
glass_csv = "glassInputs.csv"
targets_csv = "glassTargets.csv"


def read_data(file_name):
    data = pd.read_csv(file_name)
    return data


glass_data = read_data(input_folder + glass_csv)
targets_data = read_data(input_folder + targets_csv)
# %%
glass_data