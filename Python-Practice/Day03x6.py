#Write a lambda function which gives tuple of max and min from a list.

find_max_min = lambda lst: (max(lst), min(lst))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = find_max_min(numbers)

print("Max and Min:", result)