def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return first_string, second_string, False

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    sorted_first = sort(first_list)
    sorted_second = sort(second_list)

    is_anagram = sorted_first == sorted_second

    return sorted_first, sorted_second, is_anagram


def sort(list):
    list_len = len(list)
    for current_i in range(list_len - 1):
        for next_i in range(list_len - 1):
            if list[next_i] > list[next_i + 1]:
                list[next_i], list[next_i + 1] = list[next_i + 1], list[next_i]

    sorted_str = "".join(list)

    return sorted_str