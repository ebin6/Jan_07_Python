# Single inheritance


class Animals:  
    def __init__(self,a):
        self.name=a

    def info(self):
        print("Animal name : ",self.name)
    
class Dog(Animals):
    def set_breed(self,b):
        self.breed=b
    
    def displaybreed(self):
        print("Breed : ",self.breed)
    def sound(self):
        print(self.name ,"Bark ")


dg=Dog("Buddy")
dg.set_breed("lab")
dg.displaybreed()
dg.info()
dg.sound()

