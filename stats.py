def word_count(file_contents):
    """
    Gets the word count of a file.

    Args: 
        file_contents (string) : The text of a file
    
    Returns:
        int: the number of words in a file
    
    """
    words = file_contents.split()
    return len(words)

from collections import Counter
def letter_count(file_contents):

    fc = file_contents.lower()
    unique_chars = set(fc)
    count = Counter(fc)
    letters = {}

    for key in unique_chars:
        letters[key] = count[key]


    return letters

def sort_on(dict):
    return dict["count"]

def sorted_cleaned_dict(dictionary):

    alpha_dict = {}
    for key, value in dictionary.items():
        if key.isalpha() == True:
            alpha_dict[key] = value
    
    cleaned_alpha_dict = [{'char': k, 'count': v} for k, v in alpha_dict.items()]

    cleaned_alpha_dict.sort(reverse = True, key = sort_on)
    return cleaned_alpha_dict
