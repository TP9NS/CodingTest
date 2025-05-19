n = int(input())
for i in range(1,n+1):
    s = str(i)
    three= s.count('3')
    six = s.count('6')
    nine = s.count('9')
    
    total = three+six+nine
    if total ==0:
        print(i,end=" ")
    else :
        print("-"*total ,end=" ")