# utils/matcher.py
from difflib import get_close_matches
import json

def match_description_to_command(user_input, commands_list):
    """
    Match a natural language user_input to a command name using fuzzy matching on descriptions.
    """
    user_input_clean = user_input.lower().strip()
    descriptions = [cmd["description"] for cmd in commands_list]
    
    # Find the closest match with at least 0.3 similarity
    matches = get_close_matches(user_input_clean, descriptions, n=1, cutoff=0.3)
    
    if matches:
        match_desc = matches[0]
        for cmd in commands_list:
            if cmd["description"] == match_desc:
                return cmd["name"]
    
    return None

# Example usage (to test in your local environment):
if __name__ == "__main__":
    # Load PowerShell commands DB for test
    with open("app/db/powershell_commands.json", "r", encoding="utf-8") as f:
        powershell_commands = json.load(f)["powershell_commands"]

    # Load CMD commands DB for test
    with open("app/db/cmd_commands.json", "r", encoding="utf-8") as f:
        cmd_commands = json.load(f)["cmd_commands"]

    user_input_ps = "Show all running processes"
    matched_command_ps = match_description_to_command(user_input_ps, powershell_commands)

    print(f"User Input: {user_input_ps}")
    print(f"Matched PowerShell Command: {matched_command_ps}")

    user_input_cmd = "Display IP configuration"
    matched_command_cmd = match_description_to_command(user_input_cmd, cmd_commands)

    print(f"User Input: {user_input_cmd}")
    print(f"Matched CMD Command: {matched_command_cmd}")
