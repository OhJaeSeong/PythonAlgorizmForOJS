def fact(a) :
    if a == 0 :
        return 0
    if a == 1 :
        return 1
    else :
        return a*fact(a-1)

b = int(input())
c = fact(b)
print(c)