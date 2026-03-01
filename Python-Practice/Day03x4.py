#Write a recursive function to print Fibonacci series upto n terms.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_terms(n, current=0):
    if current == n:
        return
    
    print(fibonacci(current), end=" ")
    print_fibonacci_terms(n, current + 1)


num = int(input("Enter number of terms: "))

print("Fibonacci Series:")
print_fibonacci_terms(num)