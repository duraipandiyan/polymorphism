class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        c=a+b

    def __add__(self,other):
       c= self.a+self.b
       return c
obj1=Addition(10,10)
obj2=Addition(20,20)
print(obj1+obj2)
print(obj2+obj1)


class details:
    def __init__(self, name, college_fess, bus_fess):
        self.name = name
        self.college_fess = college_fess
        self.bus_fess = bus_fess

    def __add__(self, other):
        return self.college_fess + self.bus_fess + other.fine_f + other.over_all


class fine:
    def __init__(self, fine_f, over_all):
        self.fine_f = fine_f
        self.over_all = over_all
        self.fine_f + self.over_all


obj = details("durai", 25000, 20000)
obj1 = fine(2000, 3000)
print("total fess:", obj + obj1)


