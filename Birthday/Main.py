import sets

day = 0

# Question one 
print('---> set1 <---')
print(sets.set1)

ans = int(input('Is your birth day in this set?\n' +\
                'if yes, input 1, else input 0: '))

if ans == 1:
    day += 1



# Question two
print('---> set2 <---')
print(sets.set2)

ans = int(input('Is your birth day in this set?\n' +\
                'if yes, input 1, else input 0: '))

if ans == 1:
    day += 2



# Question thee 
print('---> set3 <---')
print(sets.set3)

ans = int(input('Is your birth day in this set?\n' +\
                'if yes, input 1, else input 0: '))

if ans == 1:
    day += 4


# Question four 
print('---> set4 <---')
print(sets.set4)

ans = int(input('Is your birth day in this set?\n' +\
                'if yes, input 1, else input 0: '))

if ans == 1:
    day += 8

 

# Question five 
print('---> set5 <---')
print(sets.set5)

ans = int(input('Is your birth day in this set?\n' +\
                'if yes, input 1, else input 0: '))

if ans == 1:
    day += 16

print('Your birth day is', day)