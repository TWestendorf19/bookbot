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

def get_character_counts(book_contents):
    """!
    This function gets the count of all characters in a book and stores them in
    a dict. First it converts the book contents to all lowercase.
    """
    char_dict = {}
    lowercase_book = book_contents.lower()
    # loop through each character of the book
    for char in lowercase_book:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else: 
            char_dict[char] = 1
    return char_dict

def sorton(dict):
    return dict["val"]

def get_sorted_char_counts(char_counts_dict):
    char_counts_list = []
    # loop through each key in the dict
    keys = char_counts_dict.keys()
    for key in keys:
        char_counts_list.append({'char': key, 'val': char_counts_dict[key]})
    char_counts_list.sort(reverse=True, key=sorton)
    return char_counts_list

def print_book_report(bookpath):
    """!
    This function will generate and print out a report to the terminal given a
    string path to the books .txt file
    """
    book_contents = get_book_contents(bookpath)
    word_count = get_word_count(book_contents)
    char_counts = get_character_counts(book_contents)
    sorted_chars = get_sorted_char_counts(char_counts)
    print(f"---------- Begin report of {bookpath} ----------")
    print(f"{word_count} words found in the document\n")
    for character in sorted_chars:
        if character['char'].isalpha():
            print("The '%s' character was found %i times" % (character["char"], character["val"]))
    print(f"------------------ End report ------------------")


def main():
    print_book_report("books/frankenstein.txt")

main()