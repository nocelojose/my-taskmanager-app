class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def remove_task(self, task):
        self.tasks.remove(task)
    
    def get_tasks(self):
        return self.tasks
    
def main():
    manager = TaskManager()
    manager.add_task("Feed the cat")
    manager.add_task("Gym at 3:30")
    tasks = manager.get_tasks()
    for task in tasks:
        print(task)
    
    
    
if __name__ == '__main__':
    main()