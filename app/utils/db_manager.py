import json
from pathlib import Path
from datetime import datetime

class DBManager:
    def __init__(self):
        self.db_folder = Path(__file__).resolve().parent.parent / "db"
        self.db_folder.mkdir(exist_ok=True)

        self.functions_db_file = self.db_folder / "functions_db.json"
        self.tasks_history_file = self.db_folder / "tasks_history.json"

        # יצירת קבצים אם לא קיימים
        for file in [self.functions_db_file, self.tasks_history_file]:
            if not file.exists():
                with open(file, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4)

    def load_functions(self):
        with open(self.functions_db_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_function(self, function_entry):
        functions = self.load_functions()
        functions.append(function_entry)
        with open(self.functions_db_file, "w", encoding="utf-8") as f:
            json.dump(functions, f, indent=4)

    def load_tasks_history(self):
        with open(self.tasks_history_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_task(self, task_entry):
        tasks = self.load_tasks_history()
        tasks.append(task_entry)
        with open(self.tasks_history_file, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)


if __name__ == "__main__":
    db = DBManager()

    # דוגמה לשמירת פונקציה
    function_entry = {
        "name": "create_virtualenv",
        "description": "Creates a Python virtual environment at the specified path.",
        "created_at": datetime.now().isoformat(),
        "code": "def create_virtualenv(path): ... # function code here"
    }
    db.save_function(function_entry)
    print("Saved function. Current functions DB:")
    print(db.load_functions())

    # דוגמה לשמירת משימה
    task_entry = {
        "user_input": "Create a Python virtual environment",
        "parsed_task": {"predicate": "create", "object": "a Python virtual environment"},
        "executed_at": datetime.now().isoformat(),
        "status": "success",
        "details": "Virtual environment created at ./venv"
    }
    db.save_task(task_entry)
    print("\nSaved task. Current tasks history:")
    print(db.load_tasks_history())
