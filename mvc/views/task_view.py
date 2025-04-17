class TaskView:
    @staticmethod
    def show_menu():
        print("\n=== GESTIÓN DE TAREAS ===")
        print("1. Listar tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("No hay tareas disponibles.")
            return
        for idx, task in enumerate(tasks, start=1):
            status = "✅" if task.completed else "❌"
            print(f"{idx}. [{status}] {task.title} - {task.description}")

    @staticmethod
    def get_task_input():
        title = input("Título de la tarea: ")
        description = input("Descripción de la tarea: ")
        return title, description

    @staticmethod
    def get_task_index():
        try:
            return int(input("Número de tarea: ")) - 1
        except ValueError:
            print("Entrada inválida. Debe ser un número.")
            return -1