from controllers.task_controller import TaskController

def main():
    app = TaskController()
    app.run()

if __name__ == "__main__":
    main()