from helpers import alphabet_position, rotate_character
from sys import argv, exit

def user_input_is_valid(cl_args):
    '''This function should check to see if the user's command line argument is valid.'''
    if len(cl_args) == 2:
        if cl_args[1].isdigit():
            return True
        else:
            return False
    else:
        return False

def encrypt(text, rot):
    '''This function should implement the Caesar cypher.'''
    new_text = ''
    for char in text:
        temp = rotate_character(char, rot)
        new_text = new_text + temp
    return new_text

def main():
    if user_input_is_valid(argv):
        rotation = argv[1]
        rotation = int(rotation)
        message = input("Type a message:")
        print(encrypt(message, rotation))
    else:
        print("usage: python3 caesar.py n")

if __name__ == '__main__':
    main()
