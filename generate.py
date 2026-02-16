import random

def generate_random_list(size, min_val=0, max_val=10000):
    return [random.randint(min_val, max_val) for _ in range(size)]

