import random

def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]


import random

def generate_dataset(size):
    """Generate a list of random integers between 1 and 10,000"""
    return [random.randint(1, 10000) for _ in range(size)]