todo_list = []

while True:
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(todo_list) == 0:
            print("Your list is empty!")
        else:
            for i in range(len(todo_list)):
                print(str(i + 1) + ". " + todo_list[i])

    elif choice == "2":
        task = input("Enter new task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "3":
        for i in range(len(todo_list)):
            print(str(i + 1) + ". " + todo_list[i])
        num = int(input("Enter task number to delete: "))
        todo_list.pop(num - 1)
        print("Task deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")