from core.tokenizer import Tokenizer
from core.pos_tagger import POSTagger
from core.chunker import Chunker
from core.parser import Parser
from core.planner import Planner
from core.executor import Executor
from utils.db_manager import DBManager
from datetime import datetime

def process_user_input(user_input):
    tokenizer = Tokenizer()
    tagger = POSTagger()
    chunker = Chunker()
    parser = Parser()
    planner = Planner()
    executor = Executor()
    db = DBManager()

    print(f"\n[SigurAI] Processing: '{user_input}'\n")

    # Tokenizing
    tokens = tokenizer.tokenize(user_input)
    print(f"[Tokenizer] Tokens: {tokens}")

    # POS Tagging
    tagged = tagger.tag(tokens)
    print(f"[POS Tagger] Tagged Tokens: {tagged}")

    # Chunking
    phrases = chunker.chunk(tagged)
    print(f"[Chunker] Phrases: {phrases}")

    # Parsing
    parsed_tasks = parser.parse(phrases)
    print(f"[Parser] Parsed Tasks: {parsed_tasks}")

    # Planning
    planned_tasks = planner.plan(parsed_tasks)
    print(f"[Planner] Planned Tasks: {planned_tasks}")

    # Executing
    execution_results = executor.execute(planned_tasks)
    print(f"[Executor] Results: {execution_results}")

    # Logging task to DB
    task_entry = {
        "user_input": user_input,
        "parsed_tasks": parsed_tasks,
        "planned_tasks": planned_tasks,
        "executed_at": datetime.now().isoformat(),
        "results": execution_results
    }
    db.save_task(task_entry)
    print(f"\n[SigurAI] Task logged to DB.\n")


if __name__ == "__main__":
    print("=== SigurAI CLI ===")
    while True:
        try:
            user_input = input("SigurAI> ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting SigurAI. Goodbye.")
                break
            if user_input == "":
                continue
            process_user_input(user_input)
        except KeyboardInterrupt:
            print("\nExiting SigurAI. Goodbye.")
            break
