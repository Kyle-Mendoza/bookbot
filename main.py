import sys

from stats import  get_num_words, count_characters

if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

for sys_index in range(1, len(sys.argv)):
    open_to_file_path = sys.argv[sys_index]
    with open(open_to_file_path) as f: # with for opening a file, open*(file_url_to_open)
        file_contents = f.read()

        word_count = get_num_words(file_contents)
        characters_count = count_characters(file_contents)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")    
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for character in characters_count:
            if character.isalpha(): 
                print(f"{character}: {characters_count[character]}") 
