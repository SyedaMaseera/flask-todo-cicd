from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def get_tasks():
    return jsonify(load_tasks())

@app.route('/add', methods=['POST'])
def add_task():
    data = request.json
    tasks = load_tasks()
    task = {
        'title': data['title'],
        'date': data['date']
    }
    tasks.append(task)
    save_tasks(tasks)
    return jsonify({'status': 'success', 'task': task})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Get the PORT from env variable
    app.run(host="0.0.0.0", port=port)