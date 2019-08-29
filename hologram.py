""" Check if two words are holograms.

    Holograms words are those who has the same amount of
    character of the same type no matter the position.

    For example: hello, olleh, ehllo, leloh.
    (In this solution capital letters are taking as
    equal. So, Hello and olleh are holograms to.)
"""


def holograms(a, b):
    """Function to check the condition.

    Args: a, b strings to check
    return True if they are holograms.
    """
    aux_a = a.lower()  # decapitalize
    aux_b = b.lower()  # decapitalize
    total_in_a = total_in_b = 0  # total chars of the same tipe in each string
    res = len(a) == len(b)
    if res:
        for char in aux_a:
            total_in_a = aux_a.count(char)
            total_in_b = aux_b.count(char)
            res = total_in_a == total_in_b
            if not res:
                break  # no need to iterate more if one amount differs
            if res and total_in_a == len(a):
                # if there are two long, very very long strings,
                # with the same lengths, and all chars are the same,
                # just need to iterate once and no need to go to the end.
                # Supose 'aaaaaa.....aaaaaaaaaaaaa' (many many 'a's)
                # just looking at the first and return True its OK.
                break
    return res


a = raw_input('Enter string a: ')
b = raw_input('Enter string b: ')
holograms = holograms(a, b)
print('Are {} and {} holograms?: {}'.format(a, b, holograms))
