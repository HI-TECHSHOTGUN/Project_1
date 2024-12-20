import math


def add_numbers(a, b):
    return a + b

def is_even(a):
    return a % 2 == 0

def find_max(my_list):
    if len(my_list) > 0:
        return max(my_list)
    return 0

def divide(a, b):
    if b > 0:
        return a / b
    return 0

def calculate_logarithm(x, base):
    return math.log(x, base)

def reverse_string(my_string):
    return my_string[::-1]