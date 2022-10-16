import string
from random import random as r
from random import randint as ri
from random import choice as ch
from random import choices as chs

print(round(r() * 1000))
print(ri(1, 100))
print(ch([x for x in range(100)]))
print(chs([x for x in range(100)], k=3))
print("".join(str(i) for i in chs([x for x in range(100)], k=3)))
print("".join(str(i) for i in chs(string.ascii_letters + string.digits, k=8)))
print("".join(str(i) for i in chs([x for x in string.digits], k=4)))
