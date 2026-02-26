#Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same. Sample Input ABaBCbGc Sample Output 2A 3B 2C 1G.

string = input("Enter a string: ")

counts = {}

for char in string:
    if char.isalpha():
        char = char.upper()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

for key in sorted(counts):
    print(counts[key], key)