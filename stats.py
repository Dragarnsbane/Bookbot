
def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sorted_dict(counts):
    items = []
    for char, count in counts.items():
        items.append({"char": char, "num": count})
    return sorted(items, key=lambda x: x["num"], reverse=True)