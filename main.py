import sys

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as book:
        return book.read()
    
from stats import get_num_words
from stats import get_num_letters
from stats import sort_dict

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    sorted_list = sort_dict(get_num_letters(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_list:
        current_char = letter["char"]
        if current_char.isalpha() == True:
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
        
    #print(f"Found {num_words} total words")
    #print(get_num_letters(text))
    
if __name__ == "__main__":
    main()

