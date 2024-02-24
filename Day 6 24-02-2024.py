#P1
class classn:
    def __init__(self,n):
        self.n = n
    def isprime(self):
        count = 0
        for i in range(1,self.n+1):
            if self.n%i == 0:
                count = count + 1
        if count == 2:
            return "Yes"
        else:
            return "No"
ob1 = classn(20)
ob2 = classn(13)
print(ob1.isprime())
print(ob2.isprime())
#P2
class check:
    def __init__(self,s):
        self.s = s
    def ispalindrome(self):
        if self.s == self.s[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = check("Hello")
ob2 = check("SaS")
ob1.ispalindrome()
ob2.ispalindrome()
#P3
class total:
    def __init__(self,n):
        self.n = n
    def isprime(self):
        count = 0
        for i in range(1,self.n+1):
            if self.n%i == 0:
                count = count + 1
        if count == 2:
            print("Yes")
        else:
            print("No")
    def ispalindrome(self):
        s = str(self.n)
        if s == s[::-1]:
            print("Yes")
        else:
            print("No")

ob1 = total(22)
ob2 = total(24)
ob1.isprime()
ob1.ispalindrome()
ob2.isprime()
ob2.ispalindrome()
#P4
class total:
    def __init__(self,n,s):
        self.n = n
        self.s = s
    def isprime(self):
        count = 0
        for i in range(1,self.n+1):
            if self.n%i == 0:
                count = count + 1
        if count == 2:
            print("Yes")
        else:
            print("No")
    def ispalindrome(self):
        if self.s == self.s[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = total(12,"SaS")
ob1.isprime()
ob2 = total(14,"Hello")
ob2.ispalindrome()
ob3 = total(13,"SaS")
ob3.isprime()
ob3.ispalindrome()
#P5
class dob:
    def __init__(self,date,month,year):
        self.date=date
        self.month = month
        self.year = year
    def display1(self):
        d = {1:"Jan",2:"Feb"}
        print(self.date)
        print(d[self.month])
        print(self.year)
class details(dob):
    def __init__(self,name,age,date,month,year):
        self.name = name
        self.age = age
        self.date = date
        self.month = month
        self.year = year
        super().__init__(date,month,year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)
p = details("abc",27,24,1,2001)
p.display()
p.display1()
#P6
class vehicle:
    def __init__(self,fuel):
        self.fuel = fuel
    def display3(self):
        print(self.fuel)
class motor(vehicle):
    def __init__(self,cc,fuel):
        self.cc = cc
        self.fuel = fuel
        super().__init__(fuel)
    def display2(self):
        print(self.cc)
        print(self.fuel)
class car(motor):
    def __init__(self,name,cc,fuel):
        self.name = name
        self.cc = cc
        self.fuel = fuel
        super().__init__(cc,fuel):
    def display1(self):
        print(self.name)
        print(self.cc)
        print(self.fuel)
v1 = car("BMW","300cc","Petrol")
v1.display1()
v1.display2()
v1.display3()
#P7
from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def display(self):
        pass
class b(a):
    def display(self):
        print("Class B")
class c(a):
    def display(self):
        print("Class c")

c1 = c()
c1.display()
c2 = b()
c2.display()
#P8
try:
    a = int(input())
    c= a // 2
except ZeroDivisionError:
    print("division error")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Hello")
