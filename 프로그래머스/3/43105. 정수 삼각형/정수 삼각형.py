def solution(triangle):
    dp= []
    
    dp.append(triangle[0])
    
    for i in range(1,len(triangle)):
        temp = []
        for j in range(len(triangle[i])):
            if j ==0:
                temp.append(dp[i-1][j]+triangle[i][j])
            else:
                if len(dp[i-1])<=j:
                    temp.append(dp[i-1][j-1]+triangle[i][j])
                else:
                    temp.append(max(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j]))
        dp.append(temp)
                
    reps= len(triangle)
    return  max(dp[reps-1]) 