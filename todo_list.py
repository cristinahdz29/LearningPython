listOfTasks = []


def addTask():
    taskTitle = input('What is the Title of the task?')
    taskPriority = input('What is the Priority of the task?')
    task = {
        'title': taskTitle,
        'priority': taskPriority,
    }
    listOfTasks.append(task)


def viewAllTasks():
    for i in range(len(listOfTasks)):
        task = listOfTasks[i]
        print(f"{i + 1} - {task['title']} - {task['priority']}")


def deleteTask():
    viewAllTasks()
    index = int(input('Enter task number: '))
    listOfTasks.pop(index - 1)
    viewAllTasks()


def todo():
    programRunning = True
    while programRunning:
        userInput = input("""
        Press 1 to add task 

        Press 2 to delete task 

        Press 3 to view all tasks 

        Press q to quit
        """)

        if userInput == '1':
            addTask()
        if userInput == '2':
            deleteTask()
        if userInput == '3':
            viewAllTasks()
        if userInput == 'q':
            programRunning = False


todo()
