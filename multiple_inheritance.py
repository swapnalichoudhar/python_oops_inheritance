class A:    #parebt class

    backend="using mysql,python,java.."     #initalization 
    def bk(self):                           #function declaration the self parameter is bydefaultto print the variable that we declare as a "backend"
        print("the backend is completed with",self.backend )
        
class B:    #parent class because we use here multiple class
    frontend="using HTML,CSS.."
    def ft(self):
        print("the frontend is completed", self.frontend)
        
        
class child(A,B):   #child class declaration single child class access the multiple parent class
    def show(self):
     print("website is ready..")
    
  #using object to print the class as the output  
obj=child()
obj.bk()
obj.ft()
obj.show()
