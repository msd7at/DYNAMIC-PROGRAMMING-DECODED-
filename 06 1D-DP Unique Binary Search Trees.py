#https://leetcode.com/problems/unique-binary-search-trees/
class Solution:
    def numTrees(self, n: int) -> int:
        l=[0]*(n+1)
        l[0]=1
        l[1]=1
        for i in range(2,n+1):
            l[i]=0
            for j in range(i):
                l[i]=l[i]+l[j]*l[i-j-1]
                
        return l[n]
