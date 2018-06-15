def palindrome(s):
    s = s.lower()
    n = s[::-1]

    if n == s:
        return True
    else:
        return False


def palindrome1(s):
    s = s.lower()
    n = s[::-1]

    return n == s
