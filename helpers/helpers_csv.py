import csv


def dict_to_csv(data, file_path):
    headers = data[0].keys() if data else []

    # Open the file for writing
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')
        writer.writeheader()
        writer.writerows(data)
