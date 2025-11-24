from collections import deque
def solution(s):
    answer = 0
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        wait = deque()
        for gwal in temp:
            flag = True
            if gwal in ('[','{','('):
                wait.append(gwal)
            else:
                if wait:
                    t = wait.pop()
                    if t == '[' and gwal == ']':
                        pass
                    elif t == '{' and gwal == '}':
                        pass
                    elif t == '(' and gwal == ')':
                        pass
                    else:
                        flag = False
                        break
                else:
                    flag= False
                    break
        if not wait and flag:
            answer+=1
            
                
    return answer