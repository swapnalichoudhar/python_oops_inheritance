class A:    #single parent class
    surname="choudhar"
    def show(self):
        print("my surname is", self.surname)
        
class son1(A):    #multiple child class
    def s1(self):
        print("swapnali", self.surname)
        
        
class son2(A):
    def s2(self):
        print("arun", self.surname)
        
        
#implementing object to print output of the class
ob1=son1()
ob1.s1()
ob=A()
ob.show()
