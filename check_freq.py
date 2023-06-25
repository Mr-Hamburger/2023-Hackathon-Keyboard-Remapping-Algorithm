#import distances
import test_codes
from collections import Counter



sampleletters = "abcdefghijklmnopqrstuvwxyz"
samplesymbols = "!@#$%^&*()[]{;:}"

def most_frequent_letters(data):
    letter_count = {}
    for char in data:
            #checks if the character is a letter or a specified character
        if char.isalpha():
            #turns letter to lowercase
            char = char.lower()
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1
    return letter_count


def most_frequent_symbols(data):
    symbol_count = {}
    for char in data:
         #checks if the character is a symbol
        if char in samplesymbols:
            if char in symbol_count:
                symbol_count[char] += 1
            else:
                symbol_count[char] = 1
    return symbol_count



def sorted_letter_freq(letter_counts_dict):
    keys_sorted = []
    for key, value in sorted(letter_counts_dict.items(), key=lambda item: item[1], reverse=True):
        keys_sorted.append(key + ' : ' + str(value))

    return keys_sorted


def sorted_symbol_freq(symbol_counts_dict):
    keys_sorted = []
    for key, value in sorted(symbol_counts_dict.items(), key=lambda item: item[1], reverse=True):
        keys_sorted.append(key + ' : ' + str(value))
    return keys_sorted

#closing files
test_codes.text_file_one.close()
test_codes.text_file_two.close()
test_codes.text_file_three.close()
test_codes.text_file_four.close()
test_codes.text_file_five.close()
test_codes.text_file_six.close()
test_codes.text_file_seven.close()
test_codes.text_file_eight.close()
test_codes.text_file_nine.close()
test_codes.text_file_ten.close()