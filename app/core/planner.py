class Planner:
    def __init__(self):
        """
        יכיל Matching Rules לזיהוי משימות והמרה לפעולות ביצוע.
        ניתן להרחיב את הכללים בהתאם לצרכים שלך.
        """
        self.rules = [
            {
                "predicate": "create",
                "object_contains": "virtual environment",
                "action": "function",
                "function_name": "create_virtualenv"
            },
            {
                "predicate": "install",
                "object_contains": "",
                "action": "shell",
                "command_template": "pip install {object}"
            },
            {
                "predicate": "clone",
                "object_contains": "repository",
                "action": "shell",
                "command_template": "git clone {object}"
            },
            # תוכל להוסיף כאן כללים נוספים בהמשך
        ]

    def plan(self, parsed_tasks):
        """
        קבלת הפלט מה-Parser:
        [{"predicate": "create", "object": "a Python virtual environment"}, ...]
        ומחזירה רשימת משימות מוכנות לביצוע:
        [{"type": "function", "function_name": "create_virtualenv", "params": {...}}, ...]
        """
        planned_tasks = []

        for task in parsed_tasks:
            predicate = task["predicate"].lower()
            obj = task["object"].lower()

            matched = False
            for rule in self.rules:
                if rule["predicate"] == predicate and (rule["object_contains"] in obj):
                    if rule["action"] == "function":
                        planned_tasks.append({
                            "type": "function",
                            "function_name": rule["function_name"],
                            "params": {"raw_object": task["object"]}  # בהמשך נוכל לנתח פרמטרים נוספים
                        })
                    elif rule["action"] == "shell":
                        cmd = rule["command_template"].format(object=task["object"])
                        planned_tasks.append({
                            "type": "shell",
                            "command": cmd
                        })
                    matched = True
                    break

            if not matched:
                # ברירת מחדל: החזר פקודה כ-not-implemented או הצג למשתמש
                planned_tasks.append({
                    "type": "not_implemented",
                    "details": task
                })

        return planned_tasks


if __name__ == "__main__":
    parsed_tasks = [
        {"predicate": "Create", "object": "a Python virtual environment"},
        {"predicate": "install", "object": "numpy"}
    ]

    planner = Planner()
    plan = planner.plan(parsed_tasks)

    for p in plan:
        print(p)
