class Chunker:
    def __init__(self):
        pass

    def chunk(self, tagged_tokens):
        phrases = []
        current_phrase = {"type": None, "tokens": []}
        idx = 0

        while idx < len(tagged_tokens):
            token, tag = tagged_tokens[idx]

            if tag in ["DETERMINER", "PROPER_NOUN", "NOUN"]:
                if current_phrase["type"] != "NP":
                    if current_phrase["tokens"]:
                        phrases.append(current_phrase)
                    current_phrase = {"type": "NP", "tokens": []}
                current_phrase["tokens"].append(token)

            elif tag == "VERB":
                if current_phrase["tokens"]:
                    phrases.append(current_phrase)
                current_phrase = {"type": "VP", "tokens": [token]}

            elif tag == "PREPOSITION":
                if current_phrase["tokens"]:
                    phrases.append(current_phrase)
                current_phrase = {"type": "PP", "tokens": [token]}

            elif tag == "CONJUNCTION":
                if current_phrase["tokens"]:
                    phrases.append(current_phrase)
                phrases.append({"type": "CONJUNCTION", "tokens": [token]})
                current_phrase = {"type": None, "tokens": []}

            elif tag == "PUNCTUATION":
                if current_phrase["tokens"]:
                    phrases.append(current_phrase)
                phrases.append({"type": "PUNCTUATION", "tokens": [token]})
                current_phrase = {"type": None, "tokens": []}

            else:
                if current_phrase["type"] is None:
                    current_phrase["type"] = "OTHER"
                current_phrase["tokens"].append(token)

            idx += 1

        if current_phrase["tokens"]:
            phrases.append(current_phrase)

        return phrases

if __name__ == "__main__":
    tagged = [
        ('Create', 'VERB'),
        ('a', 'DETERMINER'),
        ('Python', 'PROPER_NOUN'),
        ('virtual', 'NOUN'),
        ('environment', 'NOUN'),
        (',', 'PUNCTUATION'),
        ('and', 'CONJUNCTION'),
        ('install', 'VERB'),
        ('numpy', 'NOUN'),
        ('and', 'CONJUNCTION'),
        ('pandas', 'NOUN'),
        ('.', 'PUNCTUATION')
    ]
    chunker = Chunker()
    phrases = chunker.chunk(tagged)
    for p in phrases:
        print(f"{p['type']:12} -> {p['tokens']}")
