# hash sign to make a comment
y="bananas"
num = 5
arr = ["Vinh", "Callie", y]  #arrays are called lists
mybool = True

#output to the console
print(y)

print("My name is Vinh")
name = "Vinh"
favnum = 100

print("My name is ", name, "and my favorite number is ",favnum)
print("My name is " +name+ "and my favorite number is " +str(favnum))
print("My name is {} and my favorite number is {}.".format(name, favnum))
print(f"My name is {name} and my favorite number is {favnum}.")

#conditionals
if num > 10:
    print("big")
elif num ==10:
    print("equal")
else:
    print("small")

#tabs vs spaces
    #this is one tab
    #this is 4 space

#loops
for i in range(1,11,1):
    print(i)

for i in range(1,11):
    print(i)

for x in arr:
    print(x) #output=["Vinh","Callie","bananas"]

arr.append("I love coding")
print(arr)

arr.pop(1)
print(arr)

#functions
def sayHi():
    print("Hi")

#dictionary objects
Mydict = {
    "key":"value",
    "key2":"value2"
}
#arrays or lists are called by index
#dictionaries are called by key names
# mydict["key"] == "value"
