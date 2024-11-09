import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, mode='r', newline='\n') as file:
        text = csv.DictReader(file, delimiter=',')
        for row in text:
            ord_dict = OrderedDict(row)
            data.append(ord_dict)

    with open(OUTPUT_FILENAME, mode='w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")