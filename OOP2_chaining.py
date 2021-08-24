# class
    # template or "cookie cutter"
    # holds all the common properties of the thing we're building
# instance
    # the  actual "thing" in question
    # a single example of the class
# attributes
    # properties of the class, the pieces of information that are common to each instance
# methods
    # functionality of the class, what that thing can do


#baseball can have size, isbouncy, color, brand
    # 4-5in diameter, kinda, white, wilson
#basketball can have size, isbouncy, color, brand

class Ball:
    def __init__(self,size,bounce,color,brand="Wilson"):
        self.Size = size
        self.IsBouncy = bounce
        self.Color = color
        self.Brand = brand
        self.IsSphere = True
    def throw(self,distance):
        print(f"The ball was thrown {distance} feet.")
        return self  #returning self allows for chaining methods 

baseball = Ball(4,True,"white")
basketball = Ball(12,True,"orange","Spalding")

print(baseball.Size)
print(basketball.Size)

print(basketball.Brand)
print(baseball.Brand)

print(baseball.IsBouncy)
baseball.IsBouncy = False
print(baseball.IsBouncy)

baseball.throw(90).throw(50).throw(80)

