print("--------------------Example 01--------------------")
stock = {
    "nails": 125,
    "screws": 35,
    "wingnuts": 8,
    "washers": 24,
}

order = ["screws", "wingnuts", "clips"]


def get_batches(count, size):
    return count // size


result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)


print("--------------------Example 02--------------------")
found = {
    name: get_batches(stock.get(name, 0), 8)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}
print(found)


print("--------------------Example 03--------------------")
found = {
    name: batches for name in order if (batches := get_batches(stock.get(name, 0), 8))
}
print(found)


print("--------------------Example 04--------------------")
result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(result)


print("--------------------Example 05--------------------")
stock = {
    "nails": 125,
    "screws": 35,
    "wingnuts": 8,
    "washers": 24,
}

order = ["screws", "wingnuts", "clips"]


def get_batches(count, size):
    return count // size


found = (
    (name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8))
)

while found:
    print(next(found))
