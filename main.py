import string
import random

def generate_pass(value):
    value_size = int(value)
    letters = string.ascii_lowercase
    random_letter_list = []
    i = 0
    while i < value_size:
        i = i+1
        random_letter = random.choice(letters)
        random_letter_list.append(random_letter)
    # print(random_letter_list)
    space_between = ''
    final_password = space_between.join(random_letter_list)
    print(final_password)
    return final_password


if __name__ == '__main__':

    """To create a program that takes a number and generate a random password length of that number. Topics: random 
    module, joining strings, taking input Hint: Create a string with all characters, then take random characters from 
    it and concatenate each char to make a big string. """

    number_input = input('Enter number:\n')
    generate_pass(number_input)

