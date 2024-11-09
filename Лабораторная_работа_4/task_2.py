import json

path = 'input.json'


def task() -> float:
    with open(path, 'r') as file:
        data = json.load(file)

    summ = 0

    for item in data:
        score = item["score"]
        weight = item["weight"]
        summ += score * weight

    return round(summ, 3)


print(task())

