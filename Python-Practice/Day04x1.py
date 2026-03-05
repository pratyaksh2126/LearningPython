#Scan n values in range 0-3 and print the number of times each value has occurred.

n = int(input("Enter number of values: "))

values = []
for i in range(n):
    values.append(int(input()))

count = {0: 0, 1: 0, 2: 0, 3: 0}

for num in values:
    if num in count:
        count[num] += 1

for key in count:
    print(key, "occurred", count[key], "times")