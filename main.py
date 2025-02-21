open_to_file_path = "books/frankenstein.txt"

with open(open_to_file_path) as f: # with for opening a file, open*(file_url_to_open)
    file_contents = f.read()
    print(type(file_contents))