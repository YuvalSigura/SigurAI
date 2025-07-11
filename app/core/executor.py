import subprocess
import importlib

class Executor:
    def __init__(self):
        """
        Executor להרצת משימות בפועל:
        - קריאה לפונקציות פנימיות אם קיימות.
        - ביצוע פקודות Shell.
        """
        pass

    def execute(self, planned_tasks):
        results = []

        for task in planned_tasks:
            if task["type"] == "function":
                result = self._execute_function(task["function_name"], task.get("params", {}))
                results.append(result)

            elif task["type"] == "shell":
                result = self._execute_shell(task["command"])
                results.append(result)

            elif task["type"] == "not_implemented":
                result = f"[NOT IMPLEMENTED] Task: {task['details']}"
                print(result)
                results.append(result)

            else:
                result = f"[UNKNOWN TASK TYPE] {task}"
                print(result)
                results.append(result)

        return results

    def _execute_shell(self, command):
        """
        מריץ פקודת Shell ומחזיר פלט ותוצאה
        """
        try:
            print(f"[EXEC] Running: {command}")
            completed_process = subprocess.run(command, shell=True, text=True, capture_output=True)
            output = completed_process.stdout.strip()
            error = completed_process.stderr.strip()

            if completed_process.returncode == 0:
                print(f"[EXEC SUCCESS] {output}")
                return {"status": "success", "output": output, "command": command}
            else:
                print(f"[EXEC ERROR] {error}")
                return {"status": "error", "error": error, "command": command}

        except Exception as e:
            print(f"[EXCEPTION] {e}")
            return {"status": "exception", "error": str(e), "command": command}

    def _execute_function(self, function_name, params):
        """
        מנסה לייבא את הפונקציה מ-app/tools או app/utils ולהפעיל אותה עם פרמטרים
        """
        try:
            # דוגמה: נניח שהפונקציה קיימת במודול בשם 'tools.<function_name>'
            module_name = f"SigurAI.app.tools.{function_name}"
            module = importlib.import_module(module_name)

            func = getattr(module, function_name)
            print(f"[EXEC] Calling function: {function_name} with params: {params}")
            result = func(**params)

            print(f"[FUNC SUCCESS] {result}")
            return {"status": "success", "output": result, "function": function_name}

        except ModuleNotFoundError:
            error_msg = f"[ERROR] Module for function '{function_name}' not found."
            print(error_msg)
            return {"status": "error", "error": error_msg, "function": function_name}

        except AttributeError:
            error_msg = f"[ERROR] Function '{function_name}' not found in module."
            print(error_msg)
            return {"status": "error", "error": error_msg, "function": function_name}

        except Exception as e:
            error_msg = f"[EXCEPTION] {e}"
            print(error_msg)
            return {"status": "exception", "error": str(e), "function": function_name}


if __name__ == "__main__":
    planned_tasks = [
        {"type": "shell", "command": "echo Hello from SigurAI"},
        {"type": "function", "function_name": "create_virtualenv", "params": {"path": "venv_test"}},
        {"type": "not_implemented", "details": {"predicate": "do", "object": "something"}}
    ]

    executor = Executor()
    results = executor.execute(planned_tasks)

    for r in results:
        print(r)
