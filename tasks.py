tasks = []

def add_task(task):
    tasks.append(task)

def list_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

add_task("Finish report")
list_tasks()
