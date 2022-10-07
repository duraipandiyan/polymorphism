class myclass:
    def myfun(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("Name",name)
        print("Age",age)
        print("Address",address)
class myclass1(myclass):
    def myfun(self,arish,age,address):
        self.aris=arish
        self.age=age
        self.address=address
        print(arish,"is recentlly join java class")
        print("Age",age)
        print("Address",address)
obj=myclass1()
obj.myfun("arish",21,"tvm")


