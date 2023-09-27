from math import *

n = int(input('input amount of numbers: '))

print("enter numbers: ")

def check(a):
    if (a <= 1):
        return False
    a = int(a)
    pos = 2
    while pos <= int(sqrt(a)):
        if a % pos == 0:
            return False
        pos += 1
    return True        

Prime = []
NotPrime = []

for i in range(n):
    a = int(input())
    if check(a):    
        Prime.append(a)
    else:
        NotPrime.append(a)

if len(Prime):
    print("prime numbers: ",end = '')
    for num in Prime:
        print (num,end = ' ')        
if len(NotPrime):
    if len(Prime):
        print("\n")
    print("none prime numbers: ",end='')
    for num in NotPrime:
        print(num,end= ' ')
