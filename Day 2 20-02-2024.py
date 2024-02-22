'''
#P1
def myFun(x):
    x[0]=20
lst=[10,11,12,13,14,15]
myFun(lst)
lst[0]=100
print(lst)
'''
#P2
def evenodd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(evenodd(5))


#P3
import math
print(math.factorial(4))

#P4
Sugarcane problem
#Approach -1
t=int(input())
for i in range(t):
    n=int(input())
    x=(n*50)-((0.7)*(n*50))
    print(x)
