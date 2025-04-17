import json
import os
from models.task import Task

TASK_FILE = "todo_app/storage/task.json"

class TaskRepo:
    def load_tasks(self):
        if not os.path.exists(TASK_FILE):
            return []
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]

    def save_tasks(self, tasks):
        os.makedirs(os.path.dirname(TASK_FILE), exist_ok=True)
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)