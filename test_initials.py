from initials import get_initials

def test_get_initials():
    assert get_initials("Ozzie Smith") == "OS"
    assert get_initials("bonnie blair") == "BB"
    assert get_initials("George") == "G"
    assert get_initials("Daniel Day Lewis") == "DDL"

test_get_initials()
print("All tests passed!")
