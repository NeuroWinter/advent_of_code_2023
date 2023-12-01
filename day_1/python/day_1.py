import re
import collections

from itertools import islice


def _extract_ints(list_of_strings: list[str]) -> list[int]:
    """

    """
    rtn = []
    for line in list_of_strings:
        # print(line)
        list_of_found_ints = re.findall('\d', line)
        # print(line)
        # print(list_of_found_ints)
        if len(list_of_found_ints) == 0:
            continue
        if len(list_of_found_ints)  == 1:
           rtn.append(int(f"{list_of_found_ints[0]}{list_of_found_ints[0]}"))
        else:
           rtn.append(int(f"{list_of_found_ints[0]}{list_of_found_ints[-1]}"))
    return rtn


def challenge_one(list_of_strings: list[str]) -> int:
    """
    Convert the input into a list of integers.

    Where the input is a list of lines, where each line contains at least 2
    numbers. Combine the first and the last digit in the sequence of each line
    to form a 2 digit number.
    """
    return sum(_extract_ints(list_of_strings=list_of_strings))

def _read_input(input_file_path: str) -> list[str]:
    input_data = []
    with open(input_file_path, 'r') as in_file:
        for line in in_file.readlines():
            input_data.append(str(line))
    return input_data


def consume(iterator, n=None):
    """
    Advance the iterator n-steps ahead. If n is None, consume entirely.

    Stolen from https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def convert_string(in_str: str) -> str:
    """
    If the input string contains a word of a number then convert it to a num.
    """

    rtn_str = ''
    # we need to find the first real number so I am thinking we need to scan
    # though the string and almost make a graph.
    index_letter_tuple_list = enumerate(in_str)
    for index, letter in index_letter_tuple_list:
        if letter in ['o', 't', 'f', 's', 'e', 'n']:
            # we need to check to see if there is enough values after the index
            if len(in_str) < index + 2:
                rtn_str += letter
                continue
            if len(in_str) < index + 3:
                rtn_str += letter
                continue
            if len(in_str) < index + 4:
                rtn_str += letter
                continue
            # now lets look for the next valid number char
            if letter == 'o' and \
               in_str[index+1] == 'n' and \
               in_str[index+2] == 'e':
                rtn_str += '1'
                consume(index_letter_tuple_list, n=2)
            elif letter == 't':
                if in_str[index+1] == 'w' and \
                   in_str[index+2] == 'o':
                    rtn_str += '2'
                    consume(index_letter_tuple_list, 2)
                elif in_str[index+1] == 'h' and \
                     in_str[index+2] == 'r' and \
                     in_str[index+3] == 'e' and \
                     in_str[index+4] == 'e':
                    rtn_str += '3'
                    consume(index_letter_tuple_list, 4)
                else:
                    rtn_str += letter
            elif letter == 'f':
                if in_str[index+1] == 'o' and \
                   in_str[index+2] == 'u' and \
                   in_str[index+3] == 'r':
                    rtn_str += '4'
                    consume(index_letter_tuple_list, 3)
                elif in_str[index+1] == 'i' and \
                     in_str[index+2] == 'v' and \
                     in_str[index+3] == 'e':
                    rtn_str += '5'
                    consume(index_letter_tuple_list, 3)
                else:
                    rtn_str += letter
            elif letter == 's':
                if in_str[index+1] == 'i' and \
                   in_str[index+2] == 'x':
                    rtn_str += '6'
                    consume(index_letter_tuple_list, 2)
                elif in_str[index+1] == 'e' and \
                     in_str[index+2] == 'v' and \
                     in_str[index+3] == 'e' and \
                     in_str[index+4] == 'n':
                    rtn_str += '7'
                    consume(index_letter_tuple_list, 4)
                else:
                    rtn_str += letter
            elif letter == 'e' and \
                 in_str[index+1] == 'i' and \
                 in_str[index+2] == 'g' and \
                 in_str[index+3] == 'h' and \
                 in_str[index+4] == 't':
                rtn_str += '8'
                consume(index_letter_tuple_list, 4)
            elif letter == 'n' and \
                 in_str[index+1] == 'i' and \
                 in_str[index+2] == 'n' and \
                 in_str[index+3] == 'e':
                rtn_str += '9'
                consume(index_letter_tuple_list, 3)
            else:
                rtn_str += letter
        else:
            rtn_str += letter
    # print("*"*80)
    # print(f"in_str: {in_str}")
    # print(f"rtn_str: {rtn_str}")
    # print("*"*80)
    return rtn_str

def does_contain_number(input_str: str) -> bool:
    """
    Return True if the words 1-9 are present in the string.
    """
    if 'one' in input_str:
        return True
    elif 'two' in input_str:
        return True
    elif 'three' in input_str:
        return True
    elif 'four' in input_str:
        return True
    elif 'five' in input_str:
        return True
    elif 'six' in input_str:
        return True
    elif 'seven' in input_str:
        return True
    elif 'eight' in input_str:
        return True
    elif 'nine' in input_str:
        return True
    else:
        return False

def convert_string_but_better(in_str: str) -> str:
    """
    If the input string contains a word of a number then convert it to a num.
    """
    helper_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # Here I am going to do a form of sliding window, where I will pass in
    # a string into a function, and if it contains a word of a number
    # then replace it with that number and add that to the rtn
    # if it does not then increase the window.

    # start with a window that starts that the first index of the list
    # and ends at the second index of the list, then if that does not
    # contain a number then increase the window by one and try again.
    # if it does contain a number then replace that word with the number
    # and add that to the rtn string. Then increase the starting point of the
    # window by the length of the word that was replaced and reset the window
    # size to 1.
    rtn_str = ''
    window_start = 0
    window_end = 1
    print(f"in_str: {in_str}")
    while window_end <= len(in_str):
        window = in_str[window_start:window_end]
        print(f"window: {window}")
        if does_contain_number(input_str=window):
            print(f"found number: {window}")
            for key in helper_dict.keys():
                if key in window:
                    print(f"replacing {key} with {helper_dict[key]}")
                    window        = window.replace(key, helper_dict[key])
                    window_start += len(window) + len(key) - 2
            rtn_str += window
            window_end = window_start + 1
            print(f"rtn_str: {rtn_str}")
        else:
            window_end += 1
        # we need to add the remaning chars to the rtn_str
        if window_end > len(in_str):
            rtn_str += in_str[window_start:]
            break
    return rtn_str



def challenge_two(list_of_strings: list[str]) -> int:
    """
    Now we need to convert each word that is a number into a digit.

    EG: nine == 9, one == 1 etc
    """
    converted_strings = [convert_string_but_better(in_str=in_str).strip() for in_str in list_of_strings]
    return challenge_one(list_of_strings=converted_strings)


test_input = [
#    '1abc2',
#    'pqr3stu8vwx',
#    'a1b2c3d4e5f',
#    'treb7uchet'
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
    # 'eighthree'
    # '5qt1',
    # '5qf2',
    # '5qs3',
    # '5qel',
    # '5qnl',
    # '12twone1',
    # 'onee1twoo2threee3fourr4fivee5sixx6sevenn7eightt8ninee9'
]


# print(challenge_one(list_of_strings=test_input))

# in_data = _read_input(input_file_path='./challenge_one_input.txt')
# print(challenge_one(list_of_strings=in_data))

in_data = _read_input(input_file_path='./challenge_two_input.txt')
# print(challenge_two(list_of_strings=test_input))
print(challenge_two(list_of_strings=in_data))
