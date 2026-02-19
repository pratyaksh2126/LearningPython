num = int(input("Enter a number: "))

sum_of_powers = 0
temp = num

num_digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
