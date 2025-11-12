def get_num_words(text: str) -> int:
    word_list = []
    word_list = text.split()
    return len(word_list)

def get_num_letters(text: str) -> dict:
    num_letters = {}
    for letter in text.lower():
        if letter not in num_letters:
            num_letters[f"{letter}"] = 0
        if letter in num_letters:
            num_letters[f"{letter}"] += 1
    return num_letters

def find_num(dict: dict) -> int
    


def sort_dict(d: dict) -> list:
    temp_list = []
    for char in d:
        temp_list.add({"char": f"{char}", "num": f"{num}"})