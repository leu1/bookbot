def main():
    text = book_text("books/frankenstein.txt")
    words = word_count(text)
    print_report(text, char_count(text))

def book_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = len(text.split())
    return words

def char_count(text):

    text_char = text.lower()
    text_dict = dict()

    for t in text_char:
        if t not in text_dict:
            text_dict[t] = 1
        else:
            text_dict[t] += 1
        
    return text_dict


def sort_on(text_dict):
    return text_dict["num"]

def print_report(text, text_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document")
    text_tuple = list(text_dict.items())
    text_tuple = sorted(text_tuple, key=lambda item: item[1], reverse=True)
    for i, count in text_tuple:
        if i.isalpha():  # Ensure it is a character
            print(f"The '{i}' character was found {count} times")
    print("--- End report ---")

main()