#https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/number-of-rs-1/description/

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for q in range(t):
    s=input()
    l=[]
    c=0
    for i in s:
        if i=="R":
            l.append(-1)
            c+=1
        else:
            l.append(1)
    meh=0
    msf=min(l)
    for i in l:
        meh+=i
        if meh<i:
            meh=i
        if meh>msf:
            msf=meh
    print(c+msf)
