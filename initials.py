def get_initials(fullname):
    '''This function should take a person's full name and return the capitalized initials.'''
    temp = fullname.lower()
    empty = temp.split()
    initials = ''
    for word in empty:
        initials = initials + word[0]
    initials = initials.upper()
    #return "The initials of", fullname, "are", initials + '.'
    return initials

def main():
    fullname = input("What is your full name?\n")
    print(get_initials(fullname))

if __name__ == '__main__':
    main()
