from flask import Flask, jsonify, request

app = (__name__)

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)
        
    def get_tasks(self):
        return self.tasks
    
manager = TaskManager()

@app.route('/tasks', methods =['GET'])
def get_tasks():
    tasks = manager.get_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = data.get('task')
    if task:
        manager.add_task(task)
        return 'Task added', 201
    else:
        return 'Invalid request', 400
    
@app.route('/tasks/<task>', methods=['DELETE'])
def remove_task(task):
    try:
        manager.remove_task(task)
        return 'Task removed', 200
    except ValueError:
        return 'task not found', 400
    
if __name__=='__main__':
    app.run(debug=True)
            
    
           