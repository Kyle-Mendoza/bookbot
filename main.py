from stats import count_words, count_characters

open_to_file_path = "books/frankenstein.txt"

with open(open_to_file_path) as f: # with for opening a file, open*(file_url_to_open)
    file_contents = f.read()

    word_count = count_words(file_contents)
    
    print(f"{word_count} words found in the document")
