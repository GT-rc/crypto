from helpers import alphabet_position, rotate_character

def test_alphabet_position():
    assert alphabet_position('a') == 0, alphabet_position('a')
    assert alphabet_position("A") == 0
    assert alphabet_position("b") == 1
    assert alphabet_position("y") == 24
    assert alphabet_position("z") == 25
    assert alphabet_position("Z") == 25

def test_rotate_character():
    assert rotate_character('a', 13) == 'n'
    assert rotate_character('a', 14) == 'o'
    assert rotate_character('a', 0) == 'a'
    assert rotate_character('c', 26) == 'c'
    assert rotate_character('c', 27) == 'd'
    assert rotate_character('A', 13) == 'N'
    assert rotate_character('z', 1) == 'a'
    assert rotate_character('Z', 2) == 'B'
    assert rotate_character('!', 37) == '!'
    assert rotate_character('6', 13) == '6'

test_alphabet_position()
test_rotate_character()
print("All tests passed!")
