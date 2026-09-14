def get_stats(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum

print("Hello, I am Muhammad Shavaiz Haider, and my student ID is r02146493.")

numbers = [10, 20, 30, 40, 50]

mean, maximum = get_stats(numbers)

print("Mean:", mean)
print("Maximum:", maximum)