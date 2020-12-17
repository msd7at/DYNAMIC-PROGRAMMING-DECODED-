#https://practice.geeksforgeeks.org/problems/bbt-counter4914/1#
#User function Template for python3
class Solution:
    def countBT (self, h):
        d=[1,1]
        m=(10**9)+7
        for i in range(2,h+1):
            d.append(d[i-1]*((2*(d[i-2]%m)+d[i-1])%m)%m)
        return d[h]
