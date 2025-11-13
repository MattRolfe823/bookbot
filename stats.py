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

def sort_on(letters):
    return letters["num"]   


def sort_dict(d: dict) -> list:
    temp_list = []
    for char in d:
        temp_dict = {}
        temp_num = d[f"{char}"]
        temp_dict["char"] = char
        temp_dict["num"] = temp_num
        temp_list.append(temp_dict)
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list