def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def char_sorted(char_dict):
    items = list(char_dict.items())
    new_list = []
    for item in items:
        if item[0].isalpha():
            new_item = {"char": item[0], "count": item[1]}
            new_list.append(new_item)
        

    new_list.sort(reverse=True, key=sort_on)
    
    return new_list