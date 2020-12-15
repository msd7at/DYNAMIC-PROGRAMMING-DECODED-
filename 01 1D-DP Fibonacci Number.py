#https://leetcode.com/problems/fibonacci-number/
#recursive 
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)
        
# space and o(n)
class Solution:
    def fib(self, n: int) -> int:
        l=[0,1]
        if n==0 or n==1:
            return n
        for i in range(n-1):
            l.append(l[-1]+l[-2])
        return l[-1]
        
        
 # o(n) without space
 class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        a,b=0,1
        for i in  range(n-1):
            b,a=a+b,b
    
        return b
  # o(1)
  class Solution:
    def fib(self, N: int) -> int:
        gd=(1+ 5**0.5)/2
        return int((gd**N+1)/5**0.5)
    
