import random

def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]
