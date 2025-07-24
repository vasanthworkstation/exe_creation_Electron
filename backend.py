from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import sys

app = Flask(__name__)
CORS(app)  # Enable CORS for Electron communication

# Simple in-memory storage (in real app, use database)
tasks = []
task_id_counter = 1

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify({'tasks': tasks, 'status': 'success'})

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """Add a new task"""
    global task_id_counter
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    task = {
        'id': task_id_counter,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False
    }
    
    tasks.append(task)
    task_id_counter += 1
    
    return jsonify({'task': task, 'status': 'success'})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    data = request.get_json()
    
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['description'] = data.get('description', task['description'])
            task['completed'] = data.get('completed', task['completed'])
            return jsonify({'task': task, 'status': 'success'})
    
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'status': 'success'})

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'Backend is running!', 'python_version': sys.version})

if __name__ == '__main__':
    print("Starting Python backend server...")
    print("Server will run on http://localhost:5000")
    app.run(host='localhost', port=5000, debug=False)