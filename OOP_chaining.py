class Ball:
    def __init__(self,Type,size,bounce,color,brand="Wilson"):
        self.type = Type
        self.Size = size
        self.IsBouncy = bounce
        self.Color = color
        self.Brand = brand
        self.IsSphere = True

    def throw(self,distance):
        print(f"The ball was thrown {distance} feet.")
        return self  #returning self allows for chaining methods 

baseball = Ball("baseball",4,True,"white")
basketball = Ball("basketball",12,True,"orange","Spalding")

# print(baseball.Size)
# print(basketball.Size)

# print(basketball.Brand)
# print(baseball.Brand)

# print(baseball.IsBouncy)
# baseball.IsBouncy = False
# print(baseball.IsBouncy)

# baseball.throw(90).throw(50).throw(80)

class Animal:
    def __init__(self,name,Type,color):
        self.name = name
        self.type = Type
        self.color = color
    
    def play(self,toy):
        return f"{self.name} played with the {toy.type}."

class User:
    def __init__(self,name,email,age,healthy=True):
        self.name = name
        self.email = email
        self.age = age
        self.healthy = healthy

    def introduction(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")
        return

    def eat(self,food):
        print(f"{self.name} ate some {food}.")
        return

    def Birthday(self):
        self.age +=1
        return self

Melissa = User("Melissa","MelissaM@gmail.com",23)
Alexander = User("Alexander","AlexanderG@gmail.com",23)
Amanda = User("Amanda","arussell@codingdojo.com",29,False)

Melissa.introduction()
Alexander.introduction()
Amanda.introduction()

Melissa.eat("sushi")
Amanda.eat("yellow curry")

Alexander.Birthday()
print(Alexander.age)

Melissa.introduction()
Alexander.introduction()
Amanda.introduction()

Melissa.eat("sushi")
Amanda.eat("yellow curry")

Alexander.Birthday()
print(Alexander.age)
print(Melissa.toy.Size)
print(Melissa.toy.Color)
print(Melissa.toy.IsBouncy)

Melissa.toy.Color = "green"
print(Melissa.toy.Color)

Alexander.toy = baseball
print(Alexander.toy.Color)
print(Alexander.toy.Size)

Alexander.toy.throw(80).throw(50).throw(75)









