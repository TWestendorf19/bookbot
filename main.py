def get_book_contents(book_path):
    """!
    This function returns the contents of a book given a path to the book as a
    string
    @param bookpath: path to the book as a string
    @return book_contents: all contents of the book as a string
    """
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

def print_book_to_terminal(book_contents):
    """!
    This function reads the contents of a book given a path to the book and
    prints the book contents to the terminal
    @param book_contents: string containing all the contents of a book
    @return: n/a
    """
    print(book_contents)

def get_word_count(book_contents):
    """!
    This function takes the contents of a book and returns the word count and
    prints it to the terminal
    @param book_contents: string containing all the contents of a book
    @return word_count: number of words in book_contents
    """
    words = book_contents.split()
    word_count = len(words)
    return word_count

def main():
    frankenstein = get_book_contents("books/frankenstein.txt")
    print_book_to_terminal(frankenstein)
    word_count = get_word_count(frankenstein)
    print(f"Word count: {word_count}")

main()