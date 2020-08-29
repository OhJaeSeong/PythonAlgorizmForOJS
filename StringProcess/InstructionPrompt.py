
strNum = int(input())
inst = [0 for x in range(0,strNum)]
answer = ""
for i in range(0,strNum) :
    inst[i] = input()
for n in range(0,len(inst[0])):
    one = inst[0][n:n+1]
    for k in range(0,strNum) :
        if inst[k][n:n+1] != one :
            answer += "?"
            break;
        if k == strNum-1 :
            answer += one
print(answer)