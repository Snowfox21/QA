import random


def generate_alphanum_random_string(length):
    letters_and_digits = ''.join(chr(i) for i in range(1040, 1104))
    rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
    print(rand_string)


generate_alphanum_random_string(51)