print("--------------------Example 01--------------------")


from time import sleep
from datetime import datetime


def log(message: str, when=datetime.now()) -> print:
    print(f"{when}: {message}")


log("Hi there!")  # 2023-04-05 19:45:23.239854: Hello again!
sleep(0.1)
log("Hello again!")  # 2023-04-05 19:45:23.239854: Hello again!


print("--------------------Example 02--------------------")


def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


log("Hi there!")  # 2023-04-05 19:49:07.910633: Hi there!
sleep(0.1)
log("Hello again!")  # 2023-04-05 19:49:08.015318: Hello again!


print("--------------------Example 03--------------------")


import json


def decode(data: str, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode("bad data")
foo["stuff"] = 5

bar = decode("also bad")
bar["meep"] = 1

print("Foo:", foo)  # Foo: {'stuff': 5, 'meep': 1}
print("Bar:", bar)  # Bar: {'stuff': 5, 'meep': 1}

assert foo is bar


print("--------------------Example 04--------------------")


def decode(data: str, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo = decode("bad data")
foo["stuff"] = 5

bar = decode("also bad")
bar["meep"] = 1

print("Foo:", foo)  # Foo: {'stuff': 5}

print("Bar:", bar)  # Bar: {'meep': 1}

assert foo is not bar


print("--------------------Example 05--------------------")


from typing import Optional


def log_typed(message: str, when: Optional[datetime] = None) -> None:
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()

    print(f"{when}: {message}")


log_typed("Hi there!")  # 2023-04-05 20:02:23.979538: Hi there!
sleep(0.1)
log_typed("Hello again!")  # 2023-04-05 20:02:24.082369: Hello again!
