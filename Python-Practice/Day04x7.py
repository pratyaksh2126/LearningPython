#Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
        else:
            print("No tasks available.")

    elif choice == "3":
        if tasks:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")