print("--------------------Example 01--------------------")
import random

with open("item32_my_file.txt", "w") as f:
    for _ in range(10):
        f.write("a" * random.randint(0, 100))
        f.write("\n")


value = [len(x) for x in open("item32_my_file.txt")]
print(value)  # [67, 86, 35, 78, 73, 1, 92, 36, 25, 94]


print("--------------------Example 02--------------------")
it = (len(x) for x in open("item32_my_file.txt"))
print(it)  # <generator object <genexpr> at 0x100f98660>
print(next(it))  # 67
print(next(it))  # 86

print("--------------------Example 03--------------------")
roots = ((x, x**0.5) for x in it)
print(next(roots))  # (24, 4.898979485566356)
