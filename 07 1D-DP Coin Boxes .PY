#https://www.codechef.com/problems/CF226
import bisect
n=int(input())
m=int(input())
sec=[0]*n
for q in range(m):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    sec[l]+=1
    if r+1<n:
        sec[r+1]-=1
dp=[0]*n
dp[0]=sec[0]
for i in range(1,n):
    dp[i]=dp[i-1]+sec[i]
    
dp.sort()
q=int(input())
for a in range(q):
    s=int(input())
    print(n - bisect.bisect_left(dp, s))
