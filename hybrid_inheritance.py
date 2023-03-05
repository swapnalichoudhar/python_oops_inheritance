class A:              #combination of single and multilevel inheretance
    def show(self):
        print("class A")
        
class B(A):
    def display(self):
        print("class B")
        
class C(A):
    def prit(self):
        print("class C")
        
class D(B,C):
    def show1(self):
        print("class D")
        
        
obj=D()
obj.show()
obj.display()
obj.prit()
obj.show1()
