import string


def is_pangram(str1, alpha=string.ascii_lowercase):
    s = str1.lower()
    for char in alpha:
        if char not in s:
            return False
    else:
        return True


def is_pangram1(str1, alpha=string.ascii_lowercase):
    alphaset = set(alpha)
    return alphaset <= set(str1.lower())
