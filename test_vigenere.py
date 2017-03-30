from vigenere import encrypt
import helpers

def test_vigenere():
    assert encrypt('aaaa', 'abcd') == 'abcd', encrypt('aaaa', 'abcd')
    assert encrypt('abcd', 'bb') == 'bcde', encrypt('abcd', 'bb')
    assert encrypt('abcd', 'cd') == 'ceeg', encrypt('abcd', 'cd')
    assert encrypt('The crow flies at midnight!', 'boom') == 'Uvs osck rmwse bh auebwsih!', encrypt('The crow flies at midnight!', 'boom')
    assert encrypt('Please encrypt my sentence.', 'testing') == 'Ipwtar kggjrxg sr wwgbrtvi.', encrypt('Please encrypt my sentence.', 'testing')

test_vigenere()
print("All tests passed!")
