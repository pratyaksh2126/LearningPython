#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)

def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum


nums = list(map(int, input("Enter numbers separated by space: ").split()))

max_val, min_val = find_max_min(nums)

print("Maximum:", max_val)
print("Minimum:", min_val)