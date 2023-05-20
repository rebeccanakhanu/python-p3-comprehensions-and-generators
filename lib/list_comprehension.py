#!/usr/bin/env python3

def return_evens(num_list):
    list_even = []
    return [num for num in num_list if num % 2 ==0]
    print (list_even)

def make_exclamation(sentence_list):
   return [sentence + '!' for sentence in sentence_list]
   