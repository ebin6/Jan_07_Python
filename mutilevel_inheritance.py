class A:
    def __init__(self):
        self.a=10

class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
    
class C(B):
    def add(self):
        print(self.a+self.b)
    
oc=C()


oc.add()

    
    



