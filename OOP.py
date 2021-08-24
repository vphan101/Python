#class (or object)
    # template

#instance
#attributes
#methods

class Ball:
    def __init__(self,size,bounce,color,brand="Wilson"):
        self.Size = size
        self.IsBouncy = bounce
        self.Color = color
        self.Brand = brand
        self.IsSphere = True

    def throw(self,distance):
        print(f"The ball was thrown {distance} feet.")
        return self  #return self allows for chaining methods

baseball = Ball(4,True,"white")
basketball = Ball(12,True,"orange","Spalding")

print(baseball.Size)
print(baseball.IsBouncy)
print(baseball.Color)
print(baseball.Brand)


print(basketball.Size)
print(basketball.Color)
print(basketball.Brand)

basketball.IsBouncy = False
print(basketball.IsBouncy)

baseball.throw(90)
baseball.throw(45).throw(34).throw(70)

class Animal:
    def __init__(self,name,Type,color):
        self.name = name
        self.type = Type
        self.color = color

    def play(self,toy):
        return(f"{self.name} played with the {toy}.")

class User:
    def __init__(self,name,email,age, healthy=True):
        self.name = name
        self.email = email
        self.age = age
        self.healthy = healthy
        self.ball = Ball(5, True,"red")
        self.basketball = Ball(10,True, "black")
        self.pet = Animal("Winston","dog","brown")
    
    def introduction(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")
        return
    
    def eat(self,food):
        print(f"{self.name} ate some {food}.")
        return 

    def Birthday(self):
        self.age +=1
        return self

    def pet_time(self):
        play = self.pet.play(baseball)
        print(f"{self.name} loves {self.pet.name} and plays with him.", play)

Melissa = User("Melissa","Melissa@email.com",28)
Alexander = User("Alexander","Alexander@gmail.com",22)
Amanda = User("Amanda","Russell@gmail.com",29,False)

Ashton = User("Ashton","Ashton@gmail.com",19)
Ashton.pet_time()

Melissa.introduction()
Alexander.introduction()
Amanda.introduction()

Melissa.eat("sushi")
Amanda.eat("yellow curry")

Alexander.Birthday()
print(Alexander.age)

print(Melissa.ball.Size)
print(Melissa.ball.Color)
print(Melissa.ball.IsBouncy)

print(Melissa.basketball.Size)
print(Melissa.basketball.Color)

Melissa.ball.Color = "green"
print(Melissa.ball.Color)

Amanda.basketball.throw(80).throw(50)







    
