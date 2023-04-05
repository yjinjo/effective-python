print("--------------------Example 01--------------------")
a = [1, 2, 3]
squares = []
for x in a:
    squares.append(x**2)
print(squares)  # [1, 4, 9]

print("--------------------Example 02--------------------")
squares = [x**2 for x in a]
print(squares)  # [1, 4, 9]


print("--------------------Example 03--------------------")
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)  # [4]


print("--------------------Example 04--------------------")
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)  # {2: 4}
print(threes_cubed_set)  # {27}
