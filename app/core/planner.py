import sys
import os
from utils.matcher import match_description_to_command
from utils.db_manager import load_powershell_commands, load_cmd_commands

class Planner:
    def __init__(self):
        """
        Matching rules for direct structured tasks.
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
        ]

        # Load command DBs once
        self.powershell_commands = load_powershell_commands()
        self.cmd_commands = load_cmd_commands()

    def plan(self, parsed_tasks):
        """
        Plan tasks from parsed_tasks using structured rules and fallback to matcher for CLI.
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
                            "params": {"raw_object": task["object"]}
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
                # Use matcher fallback
                ps_match = match_description_to_command(task["object"], self.powershell_commands)
                cmd_match = match_description_to_command(task["object"], self.cmd_commands)

                if ps_match:
                    planned_tasks.append({
                        "type": "powershell",
                        "command": ps_match
                    })
                    matched = True
                elif cmd_match:
                    planned_tasks.append({
                        "type": "cmd",
                        "command": cmd_match
                    })
                    matched = True

            if not matched:
                planned_tasks.append({
                    "type": "not_implemented",
                    "details": task
                })

        return planned_tasks

if __name__ == "__main__":
    parsed_tasks = [
        {"predicate": "Create", "object": "a Python virtual environment"},
        {"predicate": "install", "object": "numpy"},
        {"predicate": "show", "object": "all running processes"},
        {"predicate": "display", "object": "ip configuration"}
    ]

    planner = Planner()
    plan = planner.plan(parsed_tasks)

    for p in plan:
        print(p)