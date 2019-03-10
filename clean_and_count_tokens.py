#!/usr/bin/python3
#
# Comp Ling PROJECT #1- Cleaning and Tokenization
# March 2019
# Author: Kelsey Broadfield kelseybroadfield@bennington.edu
#

import re
import sys
# ./clean_and_count_tokens.py <input_file> <output_file>

# open and read file
input_file = 'Wikipedia-LexicalAnalysis.xml'
output_file = 'lexical_analysis_out.txt'
with open(input_file, 'r') as my_text:
    lines = my_text.read()

    # this is my regular expression that 'cleans' the tags out
    lines = re.sub(r'<\/?(\w+|\s|=|\"|\/|-|\.|:|\'|\||\+)*>', ' ', lines)

    # below is a regular expression that finds the 'words' based solely on our class definition
    # I recognize that by using ONLY what we decided in class there are 'words'
    # in my lexical analysis that are parts of web addresses or just two letters
    # for example 'lt' and 'gt'

    # regular expression that is kind of extra bc I can't stand looking at pieces of web addresses as words
    cleaner = re.sub(r'\&\w+|{|\||}|\[|\]|\)|\(|\/|;|http(s)?|:_?|www.', ' ', lines)

    # word finder
    my_words = re.findall(r'\b[a-zA-Z]+\.?[a-zA-Z]+\'?', cleaner)

    # counts how many time each word in the cleaned xml file is used after making them all lowercase
    words = {}
    for word in my_words:
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# writes dictionary keys/values to a tupled list
words_list = []
for key, value in words.items():
    new = [key, value]
    words_list.append(new)


# creates a custom key with which to sort the list, sorts the second element in tuple[1], in descending order
# then sorts the first element [0] which are words in alphabetical order
def sorter(x):
    return -x[1], x[0]


# this sorts the list according to my custom key
words_list.sort(key=sorter)

# writes words to output file
with open(output_file, 'w') as my_text_out:
    for y in words_list:
        current_count = (str(y[0]) + '\t' + str(y[1]) + '\n')
        my_text_out.write(current_count)
    my_text_out.close()


# documentation:
# I consulted occasionally with Five/Satchel throughout this project but mostly self taught myself
# things that were more on my level/understandable to me than their work using the re and python documentation
# as well as stack overflow when i felt really stuck

