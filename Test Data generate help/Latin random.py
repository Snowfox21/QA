import random
import string

def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters
    rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
    print(rand_string)



generate_alphanum_random_string(302)