def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as book:
        return book.read()
    
from stats import get_num_words
from stats import get_num_letters

def main() -> None:
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print(get_num_letters(text))

if __name__ == "__main__":
    main()