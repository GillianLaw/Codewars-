import re

def reverse_alternate(string):
    phrase = string.split(sep=' ')
    ans = []
    ans1 = []
    for i in phrase[::2]:
        ans.append(i)
    for i in phrase[1::2]:
        ans1.append(i[::-1])

    result = [None]*(len(ans)+len(ans1))
    result[::2] = ans
    result[1::2] = ans1
    x = ' '.join(result)

    res = re.sub(' +', ' ', x)

    return res.strip()

print(reverse_alternate('This si a test'))

# Aargh, as usual codewars being a bigger. One tiny fail!





#
# def reverse_alternate(string):
#     phrase = string.split(sep=' ')
#     ans = []
#     ans1 = []
#     for i in phrase[::2]:
#         ans.append(i)
#     for i in phrase[1::2]:
#         ans1.append(i[::-1])
#
#     result = [None]*(len(ans)+len(ans1))
#     result[::2] = ans
#     result[1::2] = ans1
#
#     return ' '.join(result)
#
# print(reverse_alternate('Gillian eats hot chillis!'))