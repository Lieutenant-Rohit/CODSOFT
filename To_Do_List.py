tasks = []


def addTask():
    #Add Task to the List
    task = input("Please Enter a Task :- ")
    tasks.append(task)
    print(f"Task #{task} has been added to the list")

def listTasks():
    #List ALl Task
    if not tasks:
        print("There are no tasks added to list")
    else:
        for index, task in enumerate(tasks):
            print(f"Task #{index+1}. {task}")


def removeTask():
    #Delete Task
    listTasks()
    try:
        taskToDelete = int(input("Enter the task index number to delete: "))
        if 0 <= taskToDelete < len(tasks):
            deleted = tasks.pop(taskToDelete-1)
            print(f"Deleted Task #{taskToDelete}: {deleted}")
        else:
            print(f"Task #{taskToDelete} was not found")
    except:
        print("Invalid Input")

if __name__ == "__main__":
    # Create a loop to run app
    print("Welcome to the To-Do List!")
    while True:
        print("\n")
        print("Select one of the following options:")
        print("------------------------------------")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. List all Tasks")
        print("4. Exit")
        #Taking User Input
        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()

        elif choice == "2":
            removeTask()

        elif choice == "3":
            listTasks()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")



print("Thank You for using the App!.. Have a nice day!")