print("--------------------Example 01--------------------")


def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}", end=" ")


print_parameters(alpha=1.5, beta=9, gamma=4)  # alpha = 1.5 beta = 9 gamma = 4
