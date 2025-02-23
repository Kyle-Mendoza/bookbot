def count_words(file_content):
    book_words = file_content.split()
    word_count = len(book_words) # split accepts string and turn it intro string

    return word_count

def count_characters(file_content):
    characters_dict = {}
    sorted_dict = {} 

    for content in file_content.lower(): 
        if content not in characters_dict: 
            characters_dict[content] = 1
        else: 
            characters_dict[content] = characters_dict[content] + 1

    # This is optional, i just wanted the dictionaries to be sorted
    sorted_key = sorted(characters_dict)
    for key in sorted_key:
        if key in characters_dict:
            sorted_dict[key] = characters_dict[key]

    return sorted_dict


result = count_characters("AWDAWDAJWDADA DAWDAW awdawzzz ")

print(result)