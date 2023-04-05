print("--------------------Example 01--------------------")
from typing import List, Set, Tuple


def sort_priority(numbers: List[int], group: Set[int]):
    def helper(x: int) -> tuple:
        if x in group:
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)  # [2, 3, 5, 7, 1, 4, 6, 8]


print("--------------------Example 02--------------------")


def sort_priority2(numbers: List[int], group: Set[int]) -> bool:
    found = False

    def helper(x: int) -> Tuple:
        nonlocal found

        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)

    return found


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority2(numbers, group)
print(numbers)  # [2, 3, 5, 7, 1, 4, 6, 8]


print("--------------------Example 03--------------------")


class Sorter:
    def __init__(self, group: Set[int]):
        self.group = group
        self.found = False

    def __call__(self, x: int) -> Tuple:
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)  # [2, 3, 5, 7, 1, 4, 6, 8]
assert sorter.found is True
