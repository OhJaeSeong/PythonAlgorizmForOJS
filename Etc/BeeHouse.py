Num = int(input())
multiple = 0
if Num == 1 :
    print(1);
else :
    Num -= 1
    while Num > 0 :
        multiple += 1
        Num -= 6*multiple
    print(multiple+1)
