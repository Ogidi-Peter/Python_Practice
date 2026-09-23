def TodoList():
    list = []
    
    while True:
        Task = input("Enter your task: ")
        list.append(Task)
        message = input("Would you like to add another task (y/n): ")
        if message.lower() == 'n' or message.upper() == 'N':
            print("Your task list is: ", list)
            break
    mark = input("Would you like to mark a task as completed (y/n): ")
    if mark.lower() == 'y' or mark.upper() == 'Y':  
        completed_task = input("Enter the task you want to mark as completed: ") 
        if completed_task in list:
            list.remove(completed_task)
            print("Task marked as completed. Updated task list: ", list)

TodoList()