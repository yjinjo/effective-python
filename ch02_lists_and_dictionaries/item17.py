"""
Example 01
"""
visits = {
    "Mexico": {"Tulum", "Puerto Vallarta"},
    "Japan": {"Hakone"},
}

if (japan := visits.get("Japan")) is None:
    visits["Japan"] = japan = set()
japan.add("Kyoto")
print(visits)  # {'Mexico': {'Tulum', 'Puerto Vallarta'}, 'Japan': {'Kyoto', 'Hakone'}}


visits = {
    "Mexico": {"Tulum", "Puerto Vallarta"},
    "Japan": {"Hakone"},
}
visits.setdefault("France", set()).add("Khan")
print(
    visits
)  # {'Mexico': {'Tulum', 'Puerto Vallarta'}, 'Japan': {'Hakone'}, 'France': {'Khan'}}

"""
Example 02
"""
from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country: str, city: str):
        self.data[country].add(city)


visits = Visits()
visits.add("England", "London")
visits.add("England", "Manchester")
print(visits.data)  # defaultdict(<class 'set'>, {'England': {'London', 'Manchester'}})
