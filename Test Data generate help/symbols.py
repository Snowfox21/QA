import random
import string

def generate_random_string(length):
    digits = '!"№;%:?*()_+-=\,'
    rand_string = ''.join(random.choice(digits) for i in range(length))
    print(rand_string,  "\nthe length is", length)


generate_random_string(16)
