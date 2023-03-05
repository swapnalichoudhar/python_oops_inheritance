class A: 
    surname="choudhar"
    def sn(self):
        print("my surname is", self.surname)
        
class B(A):
    def sn1(self):
        print("swapnali", self.surname)
        
class C(B):
    def sn2(self):
        print("snehal",self.surname)
        
        
class D(C):
    def sn3(self):
        print("Arun",self.surname)
        
        
obj=D()
obj.sn()
obj.sn2()
obj.sn1()
obj.sn3()

# single paret class and multiple child classes are present
