class Employee: 
    def __init__(self,name,rank,salary):
        self.name = name
        self.rank = rank
        self.salary = salary
        
    def display_employee(self):
        print("Name: {}; Rank: {}; Salary: {}".format(self.name,self.rank,self.salary))
        
    def pay_raise(self, increment):
        self.salary += increment
    
    def promo(self, new_rank):
        self.rank = new_rank


me = Employee("gab","cp",10000)
me.display_employee()

me1 = Employee("vai","cp",10000)
me1.display_employee()

me.display_employee()