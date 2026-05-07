class Students:
    institude="OneTeam"

    def __init__(self,n):
        self.name=n

    def display(self):
        print("Hello ",self.name)


std1=Students("Ebin")
std2=Students("Aswin")


std1.display()
std2.display()