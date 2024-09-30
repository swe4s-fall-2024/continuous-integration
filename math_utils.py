from math import sqrt


def compute_sqr_root(input_val):
    if input_val < 0:
        raise ValueError(
            "Input should be a positive number. Received a negative number",
        )
    else:
        return sqrt(input_val)


def add(a, b):
    pass
