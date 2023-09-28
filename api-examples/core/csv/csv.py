import csv
import logging
from pydantic import BaseModel
from typing import List, Dict, Union


def create_csv(filer, headers: list[str], append: bool = False) -> csv.DictWriter:
    writer = csv.DictWriter(filer, fieldnames=headers)
    writer.writeheader()
    return writer

def flatten_keys(data: Union[BaseModel, Dict]) -> List[str]:
    keys = []

    if isinstance(data, BaseModel):
        data = data.dict()

    def _flatten_keys_helper(current_dict, parent_key=""):
        for key, value in current_dict.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                _flatten_keys_helper(value, new_key)
            else:
                keys.append(new_key)

    _flatten_keys_helper(data)
    return keys

def flatten_values_to_dict(data: Union[BaseModel, Dict]) -> Dict:
    flat_dict = {}

    if isinstance(data, BaseModel):
        data = data.dict()

    def _flatten_values_helper(current_dict, parent_key=""):
        for key, value in current_dict.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                _flatten_values_helper(value, new_key)
            else:
                flat_dict[new_key] = value

    _flatten_values_helper(data)
    return flat_dict
def write_csv_row(writer: csv.DictWriter, data: dict):
    writer.writerow(data)

def write_csv_rows(writer: csv.DictWriter, data: list):
    for item in data:
        write_csv_row(writer, flatten_values_to_dict(item))

def get_headers(data) -> list[str]:
    return flatten_keys(data)

def write_output(output):
    with open("output.csv", "w") as filer:
        if output:
            writer = create_csv(filer, get_headers(output[0]))
            write_csv_rows(writer, output)
        else:
            logging.error("No data to write to csv file")
