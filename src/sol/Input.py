import pandas as pd

input_folder = "../../input/"
inputs_csv = "glassInputs.csv"
targets_csv = "glassTargets.csv"
multiple_targets_csv = "glassMultipleTargets.csv"


def read_data(file_name):
    data = pd.read_csv(file_name)
    return data


def load_data():
    inputs_data = read_data(input_folder + inputs_csv)
    targets_data = read_data(input_folder + targets_csv)
    multiple_targets_data = read_data(input_folder + multiple_targets_csv)

    list_inputs = inputs_data.values.tolist()[1:]
    list_targets = targets_data.values.tolist()[1:]
    types_targets = [target[0] for target in list_targets]
    list_multiple_targets = multiple_targets_data.values.tolist()[1:]
    types_multiple_targets = [target[0] for target in list_multiple_targets]

    return list_inputs, types_targets, types_multiple_targets
