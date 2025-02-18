from flask import Flask, jsonify, request, Response
import datetime
import time
import threading
import queue

tasks = [
    {'id': 1, 'title': 'Grocery Shopping', 'completed': False, 'due_date': '2024-03-15'},
    {'id': 2, 'title': 'Pay Bills', 'completed': False, 'due_date': '2024-03-20'},
]
next_task_id = 3  # For assigning new task IDs

app = Flask(__name__)

# Queue for notifications
task_update_queue = queue.Queue()

def send_notification(task_id):
    """Simulate sending a notification asynchronously."""
    time.sleep(2)  # Simulate delay (e.g., sending an email)
    print(f"Notification sent for task {task_id}")
    task_update_queue.put(f"Task {task_id} updated")

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    global next_task_id
    data = request.get_json()
    new_task = {
        'id': next_task_id,
        'title': data['title'],
        'completed': False,
        'due_date': data.get('due_date') or datetime.date.today().strftime("%Y-%m-%d")
    }
    tasks.append(new_task)
    next_task_id += 1
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task.update(data)  # Update task attributes
            
            # Start a background thread for notification
            thread = threading.Thread(target=send_notification, args=(task_id,))
            thread.start()
            
            return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/notifications', methods=['GET'])
def event_stream():
    def generate():
        while True:
            message = task_update_queue.get()
            yield f"data: {message}\n\n"
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
