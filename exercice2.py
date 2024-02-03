__author__ = 'YEHADJI Abilé ALexis-Honoré'
__license__ = 'BSD 3 Simplified'
__version__ = '0.1.0'
__email__ = 'yehadjialexis@gmail.com'

import operator

lst1 = list(range(1200, 2000, 135)) # (1)
lst2 = [i * 2 for i in lst1 if i % 2 == 0] # (2)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

o = []
e = []

for x in numbers:
    if x % 2 == 0:
        o.append(x)
    else:
        e.append(x)

print(lst1)
print(lst2)
print(o)
print(e)
