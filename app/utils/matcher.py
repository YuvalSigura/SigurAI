# utils/matcher.py
from difflib import get_close_matches


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
    import json

    # Load PowerShell commands DB for test
    with open("app/db/powershell_commands.json", "r", encoding="utf-8") as f:
        commands_list = json.load(f)["commands"]

    user_input = "Show all running processes"
    matched_command = match_description_to_command(user_input, commands_list)

    print(f"User Input: {user_input}")
    print(f"Matched Command: {matched_command}")
