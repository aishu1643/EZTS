#P1
#Pangram
#Approach - 1
s=input()
s1=set(s)
if len(s1)==27:
    print("Pangram")
else:
    print("Not Pangram")
#Approach - 2
alpha={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s=input()
d={}
for i in s:
if i in alpha:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
x=d.keys()
print(d)
if len(x)==26:
    print("Pangram")
else:
    print("Not a pangram")
#P2
#Approach - 1
strn=input()
s=set(strn)
d={}
for i in s:
    d[i]=0
for i in strn:
    d[i]+=1
for i in d:
    if d[i]==2:
        print(i)
        break
    else:
        print(".")
#P3
#Approach - 1
n=int(input())
d={}
for i in range(n):
    name,num=input().split()
    d[name]=num
while True:
    s=input()
    if s in d:
        print(f"{s}={d[s]}")
    else:
        print("Not found")
            
#P4(Maximum word frequency)
#Approach - 1
n=int(input())
d={ }
for i in range(n):
    s=input()
    if s in d:
        d[s]=d[s]+1
    else:
        d[s]=1
x=max(d.values())
z=[]
for i in d:
    if d[i]==x:
        z.append(i)
print(max(z),x)
#P5(corrupted file)
#Approach -1 
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    d={ }
    for j in range(r):
        sid,cid=map(int,input().split())
        if cid not in d:
            d[cid]=[sid]
        else:
            d[cid].append(sid)
        for j in d:
            if len(d[j])>n and len(set(d[j]))==len(d[j]):
                print(f"Scenario #{i+1}:impossible")
                break
            else:
                print(f"Scenario #{i+1}:possible")
#P6(Directed and unweighted graph)
n=int(input())
route={}
for i in range(n):
    c1,c2=input().route()
    if c1 not in route:
        route[c1]=[c2]
    else:
        route[c1].append(c1)
print(route)
#To find the routes seperately.
city=input()
if city in route:
    print(*route[city],sep=" ")
else:
    print("None")
