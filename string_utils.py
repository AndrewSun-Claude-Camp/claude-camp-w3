# String Utils
import re

def reverse_words(text):
    words = text.split()
    return " ".join(reversed(words))

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def is_palindrome(text):
    cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    return cleaned_text == cleaned_text[::-1]
