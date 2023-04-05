print("--------------------Example 01--------------------")


def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division(1.0, 10**500, True, False)
print(result)  # 0


result = safe_division(1.0, 0, False, True)
print(result)  # inf

print("--------------------Example 02--------------------")


def safe_division_b(
    number,
    divisor,
    ignore_overflow=False,
    ignore_zero_division=False,
):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division_b(1.0, 10**500, ignore_overflow=True)
print(result)  # 0

result = safe_division_b(1.0, 0, ignore_zero_division=True)
print(result)  # inf

print("--------------------Example 03--------------------")


def safe_division_e(
    numerator,
    denominator,
    /,
    ndigits=10,
    *,
    ignore_overflow=False,
    ignore_zero_division=False,
):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division_e(22, 7)
print(result)  # 3.1428571429

result = safe_division_e(22, 7, 5)
print(result)  # 3.14286

result = safe_division_e(22, 7, ndigits=2)
print(result)  # 3.14
