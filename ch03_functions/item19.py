print("-------------------------Example 01-------------------------")


def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)

    return minimum, maximum


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths)

print(f"Min: {minimum}, Max: {maximum}")


print("-------------------------Example 02-------------------------")


def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)

    return scaled


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
longest, *middle, shortest = get_avg_ratio(lengths)

print(f"Longest:   {longest:>4.0%}")  # Longest:   108%
print(f"Shortest:  {shortest:>4.0%}")  # Shortest:   89%


print("-------------------------Example 03-------------------------")


def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)

    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum, average, median, count = get_stats(lengths)
print(f"Min: {minimum}, Max: {maximum}")  # Min: 60, Max: 73
print(
    f"Average: {average}, Median: {median}, Count {count}"
)  # Average: 67.5, Median: 68.5, Count 10
