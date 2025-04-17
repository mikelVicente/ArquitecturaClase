import json
import os

# Archivo donde se guardan las tareas
TASK_FILE = "task.json"

# Clase para representar una Tarea
class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["description"], data["completed"])

# Funciones de persistencia
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [Task.from_dict(item) for item in data]

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

# Funciones de la lógica de negocio
def list_tasks(tasks):
    if not tasks:
        print("No hay tareas disponibles.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task.completed else "❌"
        print(f"{idx}. [{status}] {task.title} - {task.description}")

def add_task(tasks):
    title = input("Título de la tarea: ")
    description = input("Descripción de la tarea: ")
    task = Task(title, description)
    tasks.append(task)
    save_tasks(tasks)
    print("Tarea agregada exitosamente.")

def mark_task_done(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Número de la tarea a marcar como completada: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx].mark_done()
            save_tasks(tasks)
            print("Tarea marcada como completada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def remove_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Número de la tarea a eliminar: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Tarea '{removed.title}' eliminada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Menú de la aplicación
def show_menu():
    print("\n=== GESTIÓN DE TAREAS ===")
    print("1. Listar tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        option = input("Seleccione una opción: ")
        if option == "1":
            list_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            mark_task_done(tasks)
        elif option == "4":
            remove_task(tasks)
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()