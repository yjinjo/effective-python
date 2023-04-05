# Example 01
counters = {
    "pumpernickel": 2,
    "sourdough": 1,
}

key = "wheat"
count = counters.get(key, 0)
counters[key] = count + 1
print(counters)  # {'pumpernickel': 2, 'sourdough': 1, 'wheat': 1}


# Example 02
votes = {
    "baguette": ["Bob", "Alice"],
    "ciabatta": ["Coco", "Deb"],
}

key = "brioche"
who = "Elmer"

if (names := votes.get(key)) is None:
    votes[key] = names = []


names.append(who)
print(
    votes
)  # {'baguette': ['Bob', 'Alice'], 'ciabatta': ['Coco', 'Deb'], 'brioche': ['Elmer']}
