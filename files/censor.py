"""
Change the word given as second parameter in the text given to *
the number of * must equal to length of word

eg:
Input: censor("this hack is wack hack", "hack")
Output: this **** is wack ****

"""


def censor(text, word):
    lisst = text.split()
    # string  = ""
    for i, akhar in enumerate(lisst):
        if akhar == word:
            lisst[i] = "*" * len(word)
        # if i < (len(lisst)-1):
        #    string = string + lisst[i] + " "
        # else:
        #    string = string + lisst[i]
    return " ".join(lisst)


print(censor("this hack is wack hack", "hack"))
