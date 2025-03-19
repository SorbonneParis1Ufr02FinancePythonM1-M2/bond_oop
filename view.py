import os

import pyexcel as pe

from helpers.helpers_csv import dict_to_csv
from helpers.helpers_serialize import dict_to_serialized_file


def to_json(data):
    output_folder = "output"
    file = "results.json"

    output_dir_path = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_dir_path, exist_ok=True)
    file_full_path = os.path.join(output_dir_path, file)

    dict_to_serialized_file(data, file_full_path)


def to_csv(data):
    output_folder = "output"
    file = "results.csv"

    output_dir_path = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_dir_path, exist_ok=True)
    file_full_path = os.path.join(output_dir_path, file)

    dict_to_csv(data, file_full_path)


def to_excel(data):
    output_folder = "output"
    file = "results.xlsx"

    output_dir_path = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_dir_path, exist_ok=True)
    file_full_path = os.path.join(output_dir_path, file)

    pe.save_as(records=data, dest_file_name=file_full_path)
