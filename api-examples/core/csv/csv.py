import csv
import logging
def create_csv(filer, headers: list[str]) -> csv.DictWriter:
    writer = csv.DictWriter(filer, fieldnames=headers)
    writer.writeheader()
    return writer

def write_csv_row(writer: csv.DictWriter, data: dict):
    writer.writerow(data.to_dict())

def write_csv_rows(writer: csv.DictWriter, data: list[dict]):
    for item in data:
        write_csv_row(writer, item)

def get_headers(data: dict) -> list[str]:
    return list(data.to_dict().keys())

def write_output(output):
    with open("output.csv", "w") as filer:
        if output:
            writer = create_csv(filer, get_headers(output[0]))
            write_csv_rows(writer, output)
        else:
            logging.error("No data to write to csv file")
