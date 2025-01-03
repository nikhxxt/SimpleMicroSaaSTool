#Flask Backend
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
