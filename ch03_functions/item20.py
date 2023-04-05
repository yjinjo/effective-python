print("-------------------------Example 01-------------------------")


def careful_divide(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print("Invalid inputs")


print("-------------------------Example 02-------------------------")


def careful_divide(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 0, 5
result = careful_divide(x, y)
if not result:
    # This runs! But shouldn't
    print("Invalid inputs")  # Invalid inputs


print("-------------------------Example 03-------------------------")


def careful_divide(a: int, b: int):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


x, y = 0, 5
success, result = careful_divide(x, y)
if not success:
    print("Invalid inputs")  # ''


print("-------------------------Example 04-------------------------")


def careful_divide(a: float, b: float) -> float:
    """Divides a by b.

    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs")


x, y = 0, 5
try:
    result = careful_divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print(f"Result is {result:.1f}")  # Result is 0.0
