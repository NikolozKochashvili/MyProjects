n = int(eval(input("enter intervar: ")))

IsPrime = [0] * (n+5)
IsPrime[1] = 1
for i in range(2,n+1):
    if IsPrime[i] == 0:
        print(i,"- Is prime")
        for j in range(i*i,n,i):
            IsPrime[j] = 1

