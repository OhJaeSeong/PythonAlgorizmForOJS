a,b,c = list(map(int, input().split()))
if b >= c :
    print(-1)
else :
    d = int(0)
    print(int(a/(c-b))+1)