"""
Example 01
"""
pictures = {}
path = "profile_1234.png"

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, "a+b")
    except OSError:
        print(f"Failed to open path: {path}")
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()

print(pictures)  # {'profile_1234.png': <_io.BufferedRandom name='profile_1234.png'>}
print(image_data)  # b''

"""
Example 02
"""
from collections import defaultdict


def open_picture(profile_path):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"Failed to open path: {profile_path}")
        raise


path = "profile_1234.png"
pictures = defaultdict(open_picture)
# handle = pictures[
#     path
# ]  # TypeError: open_picture() missing 1 required positional argument: 'profile_path'

handle.seek(0)
image_data = handle.read()


"""
Example 03
"""


def open_picture(profile_path):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"Failed to open path: {profile_path}")
        raise


class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


pictures = Pictures()
path = "profile_1234.png"
handle = pictures[path]
handle.seek(0)
image_data = handle.read()

print(pictures)  # {'profile_1234.png': <_io.BufferedRandom name='profile_1234.png'>}
print(image_data)  # b''
