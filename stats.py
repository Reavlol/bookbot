
def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def word_count(filepath):
    return len(get_book_text(filepath).split())


def character_count(filepath):
    text = get_book_text(filepath)
    chars_dict = {}
    Lower_string = text.lower()  
    for char  in Lower_string:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def dic_sort(filepath):
    char_counts = character_count(filepath)  # Get character counts
    sorted_chars = dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))
    return sorted_chars  # Return sorted list




