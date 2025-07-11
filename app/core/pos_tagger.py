class POSTagger:
    def __init__(self):
        self.verbs = {"create", "install", "delete", "remove", "run", "start", "stop", "update", "clone", "check"}
        self.conjunctions = {"and", "or", "but", "then"}
        self.determiners = {"a", "an", "the"}
        self.prepositions = {"in", "on", "at", "with", "by", "to", "for", "from", "of"}
        self.punctuation = {".", ",", "!", "?", ";", ":"}

    def tag(self, tokens):
        tagged_tokens = []
        for idx, token in enumerate(tokens):
            lower_token = token.lower()

            if token in self.punctuation:
                tagged_tokens.append((token, "PUNCTUATION"))
            elif lower_token in self.conjunctions:
                tagged_tokens.append((token, "CONJUNCTION"))
            elif lower_token in self.determiners:
                tagged_tokens.append((token, "DETERMINER"))
            elif lower_token in self.prepositions:
                tagged_tokens.append((token, "PREPOSITION"))
            elif lower_token in self.verbs or (idx == 0 and token[0].isupper()):
                tagged_tokens.append((token, "VERB"))
            elif token[0].isupper():
                tagged_tokens.append((token, "PROPER_NOUN"))
            else:
                tagged_tokens.append((token, "NOUN"))

        return tagged_tokens

if __name__ == "__main__":
    tokens = ['Create', 'a', 'Python', 'virtual', 'environment', ',', 'and', 'install', 'numpy', 'and', 'pandas', '.']
    tagger = POSTagger()
    tagged = tagger.tag(tokens)
    for token, tag in tagged:
        print(f"{token:12} -> {tag}")
