# hash sign to make comments


y="bananas"
num=6
arr=["John","Callie",y] #arrays are called lists in python
mybool= True

#output to consolep
print(y)

print("My name is Amanda.")
name="Amanda"
favnum= 100

print("My name is", name,"and my favorite number is", favnum)
print("My name is " +name+ "and my favorite number is " +str(favnum)) 


list_words = ["Hello","yes", "bye", "last"]
to_print = ""

for i in range(len(list_words)):
    to_print +=list_words[i]
    if i != len(list_words) - 1:
        to_print += ",    "

print(to_print)

list_words = ["Hello","yes", "bye", "last"]
DELIMETER = ","
print(DELIMETER.join(list_words))




    