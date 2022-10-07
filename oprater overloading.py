class leapx_org():
    def __init__(self,first,last,pay):
        self.first_n=first
        self.last_n=last
        self.pay_amt=pay
        self.fullname=first+last
    def __add__(self, other):
        result=self.pay_amt+other.pay_amt
        result=self.first_n+other.last_n+"@gmail.com"
        return result
obj1=leapx_org("durai","pandiyan",5000)
obj2=leapx_org("arish","karuna",7000)
print(obj1+obj2)


class mail:
    def __init__(self, f_name, l_name):
        self.f_n = f_name
        self.l_n = l_name
        c = self.f_n + self.l_n

    def __add__(self, other):
        c = self.f_n + other.l_n + "@gmail.come"
        return c


obj1 = mail("durai", "pandiyan")
obj2 = mail("durai", "pandiyan")
print(obj1 + obj2)


class myclass:


    def __init__(self, a, b):
        self.a = a
        self.b = b
        c=self.a+self.b

    def __add__(self, other):
        return self.a + self.b


obj1 = myclass(20, 100)
obj2 = myclass(50, 100)
print(obj1 + obj2)
print(obj2+obj1)


class myclass:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        print( self.name," salary")
        return self.salary * other.days


class plyroll:
    def __init__(self, days):
        self.days = days


obj1 = myclass("durai", 2000)
obj2 = plyroll(28)
print(obj1 * obj2)





