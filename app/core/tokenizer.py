import re

class Tokenizer:
    def __init__(self):
        self.punctuation = r"[\.,!?;:]"

    def tokenize(self, text):
        """
        Tokenizer פשוט שמפרק משפטים למילים וסימני פיסוק כטוקנים עצמאיים.
        """
        text = re.sub(f"({self.punctuation})", r" \1 ", text)
        tokens = text.strip().split()
        return tokens

if __name__ == "__main__":
    tokenizer = Tokenizer()
    sentence = "Create a Python virtual environment, and install numpy and pandas."
    tokens = tokenizer.tokenize(sentence)
    print(tokens)
