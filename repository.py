import os

from helpers.helpers_serialize import get_serialized_data


def get_data():
    input_folder = "input"
    file = "data.json"

    file_full_path = os.path.join(os.getcwd(), input_folder, file)

    return get_serialized_data(file_full_path)


if __name__ == "__main__":
    data = get_data()
    for row in data:
        print(row)
