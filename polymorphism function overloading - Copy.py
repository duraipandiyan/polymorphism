class myclass:
    def myfun(self,a):
        self.a=a                                  #function overloading
        return a                                        # is same function name with in a class pass diffrent arugumennt
                                                 # it will be run recently def function can only run:
    def myfun(self,a,b):
        self.a=a
        c=self.a=self.b
        return c
    def myfun(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        v=self.a+self.b+self.c
        return v
obj=myclass()
print("result",obj.myfun(10,20,40))




#function over loading next method
class Arith:
    def add(self,*args):
        sum=1                                       #useing *agrs we can store multiple argument
                                                     #with in class and passing multiple value in arugument
        for i in args:
            sum=sum*i
            print("mul value:",sum)

obj=Arith()
obj.add(10,20,30)



