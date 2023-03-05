class A:    #Parent Class

    num1=int(input("enter the num")) 
    num2=int(input("enter the num"))
    
    def sum(self):  #function declaration
        print("the sum is", self.num1+self.num2)
        
class B(A): #child class declaration , child inheretes the properties of parent class
    def sub(self):
        print("sub is",self.num1-self.num2 )
        
#object declaration it's play the main role to display the output of the class         
obj=A()
obj1=B()
obj.sum()
obj1.sub()
