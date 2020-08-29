a = input() 
b = input()
count = int(0)
loc = int(0)
for y in range(0,len(a)-len(b)+1) :
    if a[loc:loc+len(b)] == b :
        count += 1
        loc += len(b)
    else :
        loc += 1
print(count)
'''[ str(x) for x in input().strip().split()] 백준 1543'''