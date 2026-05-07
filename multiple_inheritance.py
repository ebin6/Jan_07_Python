class A:
    def __init__(self):
        print("Hello from methoda")
        B.__init__(self)

    
class B:
    def __init__(self):
        print("Hello from methodb")

class C(A,B):
    pass

oc=C()
