# Test String Utils

from string_utils import reverse_words, count_vowels, is_palindrome

def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("Python is fun") == "fun is Python"
    assert reverse_words("hello") == "hello"
    assert reverse_words("") == ""

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("HELLO") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("bcdfg") == 0
    assert count_vowels("") == 0

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("pop pop pop") == True
    assert is_palindrome("Was it a car or a cat I saw") == True
    assert is_palindrome("") == True
