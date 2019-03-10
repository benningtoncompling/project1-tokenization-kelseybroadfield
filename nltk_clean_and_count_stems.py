#!/usr/bin/python3
#
# Comp Ling PROJECT #1- Cleaning and Tokenization
# March 2019
# Author: Kelsey Broadfield kelseybroadfield@bennington.edu
#

import re
from nltk import word_tokenize
from nltk import stem

# ./nltk_clean_and_count_tokens.py <input_file> <output_file>

# open and read file
input_file = 'Wikipedia-LexicalAnalysis.xml'
output_file = 'lexical_analysis_nltk_stemmed_out.txt'
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

    # NLTK word tokenizer
    # doesn't work when i keep in my regular expression that identifies words?
    # not sure if this is the point but because of that, there are a lot of weird commas and stuff counted as words
    new_words = word_tokenize(cleaner)

    # adds tokenized words to a list
    final_words = []
    for x in new_words:
        final_words.append(x)
    print(final_words)

    # adds tokenized words to a list to be stemmed
    stemmed_words = []
    my_stem = stem.PorterStemmer()
    for y in final_words:
        new = my_stem.stem(y)
        stemmed_words.append(new)

    # counts how many time each word is used
    words = {}
    for word in stemmed_words:
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
    print(words_list)

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
    # NLTK