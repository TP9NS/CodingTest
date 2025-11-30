def solution(triangle):
    dp = [] #dp 테이블
    reps = len(triangle) # 삼각형 높이 = 반복 수
    
    for i in range(reps):
        if i == 0:
            dp.append([triangle[0][0]])
        else:
            temp=[]
            for j in range(len(triangle[i])):
                if j==0:
                    temp.append(triangle[i][j]+dp[i-1][j])
                elif j==len(triangle[i])-1:
                    temp.append(triangle[i][j]+dp[i-1][j-1])
                else:
                    temp.append(max(triangle[i][j]+dp[i-1][j-1],triangle[i][j]+dp[i-1][j]))
            dp.append(temp)
    return  max(dp[reps-1]) 