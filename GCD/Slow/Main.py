a = eval(input())
b = eval(input())

a, b = int(a),int(b)

while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a

print(a+b)

