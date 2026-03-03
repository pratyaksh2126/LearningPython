#(c)Variable Length Arument - 

def add_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    print("Sum:", total)

add_numbers(10, 20)
add_numbers(1, 2, 3, 4, 5)