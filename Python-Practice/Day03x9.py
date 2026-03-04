#Write a program to create two lists and generate a dictionary with keys from list1 and values from list2.

list1 = input("Enter elements of list1 separated by space: ").split()
list2 = input("Enter elements of list2 separated by space: ").split()

if len(list1) != len(list2):
    print("Lists must have same number of elements")
else:
    result_dict = {}
    
    for i in range(len(list1)):
        result_dict[list1[i]] = list2[i]
    
    print("Generated Dictionary:", result_dict)