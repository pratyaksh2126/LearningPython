#Create 2 sets s1 and s2 of n fruits each by taking input from user and find: a) Fruits which are in both sets s1 and s2 b) Fruits only in s1 but not in s2 c) Count of all fruits from s1 and s2.

n = int(input("Enter number of fruits in each set: "))

s1 = set()
s2 = set()

print("\nEnter fruits for Set 1:")
for i in range(n):
    fruit = input()
    s1.add(fruit)

print("\nEnter fruits for Set 2:")
for i in range(n):
    fruit = input()
    s2.add(fruit)

both = s1.intersection(s2)

only_s1 = s1.difference(s2)

total_count = len(s1.union(s2))

print("\nFruits in both sets:", both)
print("Fruits only in Set 1:", only_s1)
print("Total count of unique fruits:", total_count)