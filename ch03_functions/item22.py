print("--------------------Example 01--------------------")


def log(message: str, values: list[int]) -> print:
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log("My numbers are", [1, 2])  # My numbers are: 1, 2
log("Hi there", [])  # Hi there


print("--------------------Example 02--------------------")


def log(message: str, *values) -> print:
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log("My numbers are", [1, 2])  # My numbers are: 1, 2
log("Hi there", [])  # Hi there


print("--------------------Example 03--------------------")


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
