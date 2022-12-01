import string


def alphabet_position(s):
    s = s.lower()
    l = []
    for i in s:
        if i.isalpha():
            l.append(str((string.ascii_lowercase.index(i)+1)))
    return(" ".join(l))


print(alphabet_position("srikanth"))
