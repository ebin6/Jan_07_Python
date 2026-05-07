class Manager:
    def work(self):
        print("Manager manages tasks")

class Employee(Manager):
    def work(self):
        print("Employees works")

emp=Employee()

emp.work()