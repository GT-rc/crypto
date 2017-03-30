from helpers import alphabet_position, rotate_character

def encrypt(message, key):
    '''This function should implement the Vigenere cypher.'''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ''
    i = 0
    for char in message:
        if char.isalpha():
            temp = rotate_character(char, alphabet_position(key[i]))
            new_message = new_message + temp
            i = (i + 1) % len(key)
        else:
            new_message = new_message + char
    return new_message

def main():
    user_message = input("Type a message:")
    user_key = input("Encryption key:")
    print(encrypt(user_message, user_key))

if __name__ == '__main__':
    main()
