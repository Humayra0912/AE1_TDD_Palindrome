def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    return word == word[::-1]