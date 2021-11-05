import pandas as pd

input_folder = "../input/"
glass_csv = "glassInputs.csv"
targets_csv = "glassTargets.csv"


def read_data(file_name):
    data = pd.read_csv(file_name)
    return data


def load_data():
    glass_data = read_data(input_folder + glass_csv)
    targets_data = read_data(input_folder + targets_csv)
    return glass_data, targets_data