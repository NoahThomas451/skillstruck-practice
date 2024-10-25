def to_weird_case(words):
    empty = ""
    for words in range(len(words)):
        if words.index() % 2 == 0:
            return empty.join(words.upper())
        elif words.index() % 2 == 1:
            return empty.join(words.lower)