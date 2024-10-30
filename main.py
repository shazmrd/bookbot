def main():
    # Path to the book
    book_path = "books/frankenstein.txt"  
    # Read the book text
    text = get_book_text(book_path)
    # Get the number of words in the text
    num_words = get_num_words(text)
    # Get the dictionary of characters and their counts
    chars_dict = get_chars_dict(text)
    # Print the report
    print_report(book_path, num_words, chars_dict)

def get_num_words(text):
    # Split the text into words and count them
    words = text.split()  
    return len(words)

def get_chars_dict(text):
    # Create an empty dictionary for character counts
    chars = {}  
    for c in text:
        # Convert character to lowercase and strip whitespace
        lowered = c.lower().strip()  
        # Update the dictionary with character counts
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    # Read the book text from a file
    with open(path) as f:  
        return f.read()

def sort_on(d):
    # Return the number of occurrences of a character
    return d["num"]  

def chars_dict_to_sorted_list(num_chars_dict):
    # Convert character dictionary to a sorted list of dictionaries
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)  # Sort list by character count in descending order
    return sorted_list

def print_report(book_path, num_words, char_dict):
    # Prepare the report
    report = f"--- Begin report of {book_path} --- \n{num_words} words found in the document\n\n"
    new_list = chars_dict_to_sorted_list(char_dict)
    for char in new_list:
        report += f"The {char['char']} character was found {char['num']} times\n"  # Corrected the double quotes inside the f-string
    report += "--- End report ---"
    # Print the report
    print(report)

# Call the main function
main()
