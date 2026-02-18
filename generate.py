import random

def generate_random_list(size):
    """
    Generates a list of random integers.
    
    :param size: Number of elements in the list
    :return: List of random integers
    """
    return [random.randint(1, 10000) for _ in range(size)]

 ***What This Does

Imports Python’s built-in random module

Creates a function called generate_random_list

Takes size as input

Returns a list of random numbers between 1 and 10,000