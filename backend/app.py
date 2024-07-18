from flask import Flask, jsonify, request

app = (__name__)

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def add_task(self, task):
        self.tasks.remove(task)
        
    def get_tasks(self):
        return self.tasks
    
manager = TaskManager()

@app.route('/tasks', methods =['GET'])
def get_tasks():
    tasks = manager.get_tasks()
    return jsonify(tasks)
    
           