from collections import Counter

def check_palindrome(s):
    return sum( ch % 2 for ch in Counter(s).values()) <= 1

print(check_palindrome("dokilolokido"))
