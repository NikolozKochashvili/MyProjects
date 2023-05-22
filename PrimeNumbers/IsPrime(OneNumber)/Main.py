from sys import *
from math import *

n = int(input('input number: '))

for i in range(1,int(sqrt(n))):
    if (n % i == 0):
        print('it is not prime...')
        exit()
        
print('it is prime')