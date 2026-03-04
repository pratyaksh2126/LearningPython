#Write a program to check whether all the values in a dictionary are same or not using lambda function.

check_same_values = lambda d: len(set(d.values())) == 1

data = {}
n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

if check_same_values(data):
    print("All dictionary values are same")
else:
    print("Dictionary values are not same")