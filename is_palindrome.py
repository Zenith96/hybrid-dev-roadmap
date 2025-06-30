"""
Write a function is_palindrome(s) that checks if a
string is a palindrome (same forwards and backwards),
ignoring spaces and case.
"""
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
Num = input("Your String: ")
print("Is palindrome-->",is_palindrome(Num))
