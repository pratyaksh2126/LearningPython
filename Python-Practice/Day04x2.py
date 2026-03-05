#Create a tuple to store n numeric values and find average of all values.

n = int(input("Enter how many numbers: "))

numbers = []
for i in range(n):
    numbers.append(float(input()))

num_tuple = tuple(numbers)

average = sum(num_tuple) / len(num_tuple)

print("Tuple:", num_tuple)
print("Average:", average)