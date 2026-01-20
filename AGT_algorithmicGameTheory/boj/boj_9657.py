# 9657. 돌 게임 3
# https://www.acmicpc.net/problem/9657

import sys
sys.setrecursionlimit(2*10**3)

def mex(g1, g2, g3):
    if(g1 == 0 or g2 == 0 or g3 == 0):
        return 1
    
    return 0

def grundy(num):
    if(num < 0): return 1 # [0, inf)
    if(dp[num] != False): return dp[num] # dp

    dp[num] = mex(grundy(num-1), grundy(num-3), grundy(num-4))
    return dp[num]

# main
num = int(input())
dp = [False]*(num+1) # [ False | unvisited ], [ 0 | CY ], [ 1 | SK ]

print("SK" if grundy(num) == 1 else "CY")