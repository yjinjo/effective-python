print("--------------------Example 01--------------------")
from typing import List


def normalize(numbers: List[int]):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0


print("--------------------Example 02--------------------")
path = "item31_my_numbers.txt"
with open(path, "w") as f:
    for i in (15, 35, 80):
        f.write(f"{i}\n")


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits("item31_my_numbers.txt")
percentages = normalize(it)
print(percentages)  # []


print("--------------------Example 03--------------------")


def normalize_copy(numbers):
    numbers_copy = list(numbers)  # Copy the iterator
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result


it = read_visits("item31_my_numbers.txt")
percentages = normalize_copy(it)
print(percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]


print("--------------------Example 04--------------------")


def normalize_func(get_iter):
    total = sum(get_iter())  # new iterator
    result = []
    for value in get_iter():  # new iterator
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


path = "item31_my_numbers.txt"
percentages = normalize_func(lambda: read_visits(path))
print(percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]


print("--------------------Example 05--------------------")


class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize(numbers: list[int]) -> list[float]:
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


path = "item31_my_numbers.txt"
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]


print("--------------------Example 06--------------------")
from collections.abc import Iterator


def normalize_defensive(numbers: list[int]) -> list[float]:
    if isinstance(numbers, Iterator):
        raise TypeError("Must supply a container")

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize_defensive(visits)
print(percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]

path = "item31_my_numbers.txt"
visits = ReadVisits(path)
percentages = normalize_defensive(visits)
print(percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]

visits = [15, 35, 80]
it = iter(visits)
normalize_defensive(it)  # TypeError: Must supply a container
