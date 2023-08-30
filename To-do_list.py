# tasks list where user will place its tasks
tasks_list = []

# the function which adds tasks to the list
def add_task():
    task = input("Enter the tasks you want to add:\n")
    tasks_list.append(task)
    print(f"Task '{task}' added successfully!")

# the function which will view tasks to the user
def view_tasks():
    if not tasks_list:
        print("There are no tasks yet.")
    else:
        print("The tasks that you've entered so far are:\n")
        for index, task in enumerate(tasks_list, start=1):
            print(f"{index}- {task}")


# the function to remove any already added tasks
def remove_task():
    if not tasks_list:
        print("No tasks in the list yet.")
    else:
        print(view_tasks())
        try:
            task_index = int(input("Enter the index of the task you want to remove: "))-1

            if 0 <= task_index < len(tasks_list):
                removed_task = tasks_list.pop(task_index)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid index. No task removed!")
        except ValueError:
            print("Invalid input. Please, enter a valid index (number).")
            

# Main user interface loop
while True:
    print("\n--- TO-DO LIST MENU ---")
    print("\n1. Add a task")
    print("2. Remove a task")
    print("3. View Tasks")
    print("4. Exit the program")

    choice = input("\nEnter your choice 1/2/3/4 : ")
    print("")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting the application!\n")
        break
    else:
        print("Invalid choice. Please try again!")
