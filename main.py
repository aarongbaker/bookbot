from stats import word_count, letter_count, sorted_cleaned_dict
import sys
def get_book_text(path_to_file):
    """
    Gets the text from a file.

    Args: 
        path_to_file (string) : The relative path of the file containing the text
    
    Returns: 
        file_contents (string) : The text in the file
    
    """
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    #path_to_file = "books/frankenstein.txt"
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(sys.argv[1])
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    letter_count_dict = letter_count(book_text)
    cleaned_alpha_dict = sorted_cleaned_dict(letter_count_dict)
    for item in cleaned_alpha_dict:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
    
    

if __name__ == "__main__":
    # This is the main entry point of the program
    # It will call the main function to execute the program
    main()
