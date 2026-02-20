terms = int(input("Enter number of terms: "))

a, b = 0, 1

if terms <= 0:
    print("Please enter a positive number.")
elif terms == 1:
    print("Fibonacci series:")
    print(a)
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b
