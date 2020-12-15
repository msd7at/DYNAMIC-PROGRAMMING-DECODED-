#https://www.geeksforgeeks.org/ways-paint-stairs-two-colors-two-adjacent-not-yellow/

n=int(input()
l=[2,3]
if n==1 or n==2:
  print(l[n-1])
 else:
  for i in range(n-2):
    l.append(l[-1]+l[-2])
 print(l[-1])
