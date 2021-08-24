import turtle
x=5
y="string"
f=5.5

Vinh = turtle.Turtle()

print(y.upper())
print(y.replace("r", ""))

def funct(x):
    return x +2

print(funct(5))


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list = [1,3,5]
        

    def speak(self):
        print("Hi I am", self.name,"and I am ", self.age,"years old.")

    def change_age(self, age):
        self.age = age
        print("My new age is ",self.age)

    def add_weight(self, weight):
        self.weight = weight
        print("I weigh", self.weight, "pounds.")

Vinh = Dog("Vinh", 45)
Michelle = Dog("Michelle",25)

Vinh.speak()
Michelle.speak()

Vinh.change_age(10)
Vinh.speak()

Vinh.add_weight(70)
Vinh.speak()
print(Vinh.weight)

print(Vinh.age)