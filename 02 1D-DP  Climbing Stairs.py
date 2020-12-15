#https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        l=[0,1]
        if n==1:
            return n
        for i in range(n):
            l.append(l[-1]+l[-2])
        return l[-1]
