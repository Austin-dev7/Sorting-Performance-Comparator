import time

def measure_time(sort_function, data):
    """
    Measures the execution time of a sorting function.

    :param sort_function: The sorting function to test
    :param data: The dataset to sort
    :return: Time taken in seconds
    """
    start_time = time.perf_counter()
    sort_function(data.copy())  # use copy so original data is not changed
    end_time = time.perf_counter()

    return end_time - start_time
