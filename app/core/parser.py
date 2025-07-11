class Parser:
    def __init__(self):
        pass

    def parse(self, phrases):
        """
        מקבל רשימת צירופים מה-Chunker ומחזיר רשימת משימות בפורמט:
        [{'predicate': str, 'object': str}]
        """
        tasks = []
        current_task = {"predicate": None, "object": ""}

        idx = 0
        while idx < len(phrases):
            phrase = phrases[idx]

            if phrase["type"] == "VP":
                # סיום משימה קודמת אם היתה
                if current_task["predicate"]:
                    current_task["object"] = current_task["object"].strip()
                    tasks.append(current_task)
                    current_task = {"predicate": None, "object": ""}

                # שמור את הפועל כ-Predicate
                current_task["predicate"] = " ".join(phrase["tokens"])

            elif phrase["type"] == "NP":
                # הוסף את ה-Noun Phrase כמושא ישיר
                current_task["object"] += " " + " ".join(phrase["tokens"])

            elif phrase["type"] == "CONJUNCTION":
                # סיום משימה אם יש Predicate
                if current_task["predicate"]:
                    current_task["object"] = current_task["object"].strip()
                    tasks.append(current_task)
                    current_task = {"predicate": None, "object": ""}

            # If necessary, PP, PUNCTUATION, etc. can also be addressed.

            idx += 1

        # Add the last task if it exists
        if current_task["predicate"]:
            current_task["object"] = current_task["object"].strip()
            tasks.append(current_task)

        return tasks


if __name__ == "__main__":
    phrases = [
        {"type": "VP", "tokens": ["Create"]},
        {"type": "NP", "tokens": ["a", "Python", "virtual", "environment"]},
        {"type": "PUNCTUATION", "tokens": [","]},
        {"type": "CONJUNCTION", "tokens": ["and"]},
        {"type": "VP", "tokens": ["install"]},
        {"type": "NP", "tokens": ["numpy"]},
        {"type": "CONJUNCTION", "tokens": ["and"]},
        {"type": "NP", "tokens": ["pandas"]},
        {"type": "PUNCTUATION", "tokens": ["."]}
    ]

    parser = Parser()
    tasks = parser.parse(phrases)

    for task in tasks:
        print(f"Predicate: {task['predicate']}, Object: {task['object']}")
