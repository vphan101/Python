#tuple: can't be changed or modified

coordinates = [(4, 5),(6,7),(80,34)]
print(coordinates)

#Functions
def sayhi():
    print("Sup User")


sayhi()  #output: Sup User


def sayhello(name, age):
    print("Hello", name, "you are ",str(age))

sayhello("Mike", 15)  #output: Hello Mike


#Boolean

is_male = True

if is_male or is_tall:
    print("You are a male or tall or both.")  #output: You are a male or tall or both
    print("You are cool.")
else:
    print("You are neither.")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2>= num1 and num2>= num3:
        return num2
    else:
        return num3
print(max_num(300, 40, 5))
print(max_num(4,35,60))

#Calculator

