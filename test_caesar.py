from caesar import encrypt
import helpers

def test_caesar():
    assert encrypt('a', 13) == 'n'
    assert encrypt('abcd', 13) == 'nopq'
    assert encrypt('LaunchCode', 13) == 'YnhapuPbqr', encrypt("LaunchCode", 13)
    assert encrypt('LaunchCode', 1) == 'MbvodiDpef'
    assert encrypt('Hello, World!', 5) == 'Mjqqt, Btwqi!', encrypt('Hello, World!', 5)

test_caesar()
print("All tests passed!")
