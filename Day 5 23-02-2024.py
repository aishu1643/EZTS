#P1(Odd even index)
#Approach - 1
s=input()
n=len(s)
es=""
os=""
for i in range(n):
    if i%2==0:
        es=es+s[i]
    else:
        os=os+s[i]
print(os+es)
#Approach - 2
s=input()
os=s[1::2]
es=s[::2]
print(os+es)
#Approach - 3
s=input()
print(s[1::2]+s[::2])
#P2(Occurence of a character)
#Approach - 1
s=input()
ch=input(s)
print(s.count(ch))

#Approach - 2
s=input()
c=0
ch=input()
for i in range(len(s)):
    if s[i]==ch:
        c=c+1
print(c)

#Approach - 3
s=input()
c=0
ch=input()
for i in s:
    if s[i]==ch:
        c=c+1
print(c)
#P3(to print only even index positions)
#Approach -1
s=input()
c=0
ch=input()
for i in range(len(s)):
    if s[i]==ch and i%2==0:
        c=c+1
print(c)
#P4(To check whether vowels are present in the given string)
#Approach -1
s=input()
v="aeiouAEIOU"
c=0
for i in s:
    if i in v:
        c=c+1
if c==len(s):
    print("Yes")
else:
    print("NO")

#Approach - 2
s= input()
v="aeiouAEIOU"
c=0
for i in s:
    if i not in v:
        c=c+1
if c==0:
    print("Yes")
else:
    print("No")

#Approach - 3
s=input()
v="aeiouAEIOU"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")
#P5(Digits in a string)
#Approach - 1
s=input()
d="12345678910"
c=0
for i in s:
    if i in d:
        c=c+1
if c==len(s):
    print("Yes")
else:
    print("No")

#Approach - 2
s=input()
d="0123456789"
c=0
for i in s:
    if i not in d:
        c=c+1
if c==0:
    print("Yes")
else:
    print("No")
 
#Approach - 3
s=input()
d="012345689"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")

#Approach - 4
s=input()
if s.isdigit():
    print("True")
else:
    print("False")
#P6(count of vowels and consonants)
#Approach - 1
s=input()
v=0
c=0
vo="aeiouAEIOU"
for i in s:
    if i in vo:
        v+=1
    else:
        c+=1
print(v,c)

#Approach - 2
s=input()
v="aeiou"
c="qwrtyplkjhgfdszxcvbnm"
s=s.lower()
vc=0
cc=0
for i in s:
    if i in v:
        vc=vc+1
    elif i in vc:
        cc=cc+1
print(vc,cc)
#Approach - 3
s=input()
vc=0
cc=0
v="aeiouAEIOU"
for i in s:
    if i.isalpha():
        if i in v:
            vc=vc+1
        else:
            cc=cc+1
print(vc,cc)
