# Write a program to count and display the number of capital letters in a given string.

text = input("Enter a string: ")

capital_count = 0

for char in text:
    if char.isupper():   
        capital_count += 1

print("Number of capital letters:", capital_count)
