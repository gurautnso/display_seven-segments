from lib import *

vt = []
n = input('Digite uma sequência de números: ')
for i in n:
    vt.append(int(i))
n = vt[:]
for i in range(1, 6):
    for c in n:
        print(numbers(i, c), end=' ')
    print()
