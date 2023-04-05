class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


tools = [
    Tool("level", 3.5),
    Tool("hammer", 1.25),
    Tool("screwdriver", 0.5),
    Tool("chisel", 0.25),
]


print(
    f"Unsorted: {repr(tools)}"
)  # Unsorted: [Tool('level', 3.5), Tool('hammer', 1.25), Tool('screwdriver', 0.5), Tool('chisel', 0.25)]
tools.sort(key=lambda x: x.weight)
print(
    f"Sorted: {repr(tools)}"
)  # Sorted: [Tool('chisel', 0.25), Tool('screwdriver', 0.5), Tool('hammer', 1.25), Tool('level', 3.5)]


# ------------------------------------------------------------------------
saw = (5, "circular saw")
jackhammer = (40, "jackhammer")
print(jackhammer < saw)  # False


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


power_tools = [
    Tool("drill", 4),
    Tool("circular saw", 5),
    Tool("jackhammer", 40),
    Tool("sander", 4),
]
power_tools.sort(key=lambda x: (x.weight, x.name))
print(
    power_tools
)  # [Tool('drill', 4), Tool('sander', 4), Tool('circular saw', 5), Tool('jackhammer', 40)]
