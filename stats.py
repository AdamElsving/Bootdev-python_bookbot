def get_num_words(text:str) -> int:
    return len(text.split())

def get_count_characters(text:str):
    lower_cased = text.lower()
    char_dict = {}

    for char in lower_cased:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_on(char_count:tuple[str, int]) -> int:
    return char_count[1]


def char_dict_to_sorted_list(char_dict:dict[str, int]) -> list[tuple[str, int]]:
    char_counts = []

    for char, count in char_dict.items():
        char_counts.append((char, count))

    sorted_counts = sorted(char_counts, key=sort_on, reverse=True)
    return sorted_counts

