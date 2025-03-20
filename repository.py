import os

from helpers.helpers_serialize import get_serialized_data


def get_config():
    input_folder = "input"
    file = "config.yaml"
    file_full_path = os.path.join(os.getcwd(), input_folder, file)
    return get_serialized_data(file_full_path)


def get_data(config):
    input_folder = config["folders"]["input_folder"]
    file = config["files"]["input_file"]

    file_full_path = os.path.join(os.getcwd(), input_folder, file)

    return get_serialized_data(file_full_path)


if __name__ == "__main__":
    config = {"folders": {"input_folder": "input"},
              "files": {"input_file": "data.json"}}
    data = get_data(config)
    for row in data:
        print(row)
