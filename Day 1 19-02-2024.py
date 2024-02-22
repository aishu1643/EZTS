#1 largest in 2
a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)
#2 largest in 3
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)
#3 2nd largest in two
a=int(input())
b=int(input())
if a>b:
    print(b)
else:
    print(a)
#4 2nd largest in 3
a=int(input())
b=int(input())
c=int(input())
if (a>b and a<c) or (a>c and a<b):
    print(a)
elif(b>a and b<c) or (b>c and b<a):
    print(b)
else:
    print(c)
#5
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>c and b>a:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)
#6
for i in range(1000):
    print("Hello World")
#
print("Hello World\n"*1000)
#7
a,b=map(int,input().split())
if a>b:
    print("a > b")
elif a<b:
    print("a < b")
else:
    print("a == b")
#8 triangle valid or not
a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")
#9 dividde the apples 2
n,k = map(int,input().split())
print(k%n)
while(k>=n):
    k-=n
print(k)
#number reverse
n = int(input())
rev=0
if(n<0):
    n= -n
    while(n):
        y=n%10
        rev=rev*10+y
        n=n//10
    rev = -rev
else:
    while(n):
        y=n%10
        rev=rev*10+y
        n=n//10
print(rev)
#watermelon
w = int(input())
if w%2==0 and w>2:
    print("YES")
else:
    print("NO")
