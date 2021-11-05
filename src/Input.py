import pandas as pd

input_folder = "../input/"
inputs_csv = "glassInputs.csv"
targets_csv = "glassTargets.csv"


def read_data(file_name):
    data = pd.read_csv(file_name)
    return data


def load_data():
    inputs_data = read_data(input_folder + inputs_csv)
    targets_data = read_data(input_folder + targets_csv)
    
    list_inputs = inputs_data.values.tolist()[1:]
    list_targets = targets_data.values.tolist()[1:]
    
    return list_inputs, list_targets