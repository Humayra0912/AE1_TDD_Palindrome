from main import is_palindrome

def test_palindrome_returns_true():
    assert is_palindrome("otto") is True

def test_non_palindrome_returns_false():
    assert is_palindrome("hello") is False

def test_palidrome_checks_ignore_case():
    assert is_palindrome("Otto") is True

def test_palindrome_checks_ignore_space():
    assert is_palindrome("Taco Cat") is True