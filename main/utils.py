from string import ascii_lowercase, digits
from random import randint


def generate_random_string(length=10):
    """
    Generate a random string of fixed length
    """
    # Choose from all lowercase letter
    letters = ascii_lowercase + digits
    return "".join([letters[randint(0, len(letters) - 1)] for _ in range(length)])
