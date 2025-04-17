from models.task import Task
from views.task_view import TaskView
from storage.task_repo import TaskRepo

class TaskController:
    def __init__(self):
        self.repo = TaskRepo()
        self.view = TaskView()
        self.tasks = self.repo.load_tasks()

    def run(self):
        while True:
            self.view.show_menu()
            option = input("Seleccione una opción: ")
            if option == "1":
                self.view.show_tasks(self.tasks)
            elif option == "2":
                title, description = self.view.get_task_input()
                self.tasks.append(Task(title, description))
                self.repo.save_tasks(self.tasks)
                print("Tarea agregada.")
            elif option == "3":
                self.view.show_tasks(self.tasks)
                idx = self.view.get_task_index()
                if 0 <= idx < len(self.tasks):
                    self.tasks[idx].mark_done()
                    self.repo.save_tasks(self.tasks)
                    print("Tarea marcada como completada.")
            elif option == "4":
                self.view.show_tasks(self.tasks)
                idx = self.view.get_task_index()
                if 0 <= idx < len(self.tasks):
                    removed = self.tasks.pop(idx)
                    self.repo.save_tasks(self.tasks)
                    print(f"Tarea '{removed.title}' eliminada.")
            elif option == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")