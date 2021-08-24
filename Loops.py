for x in range(0, 10, 2):
    print(x)

for x in range(0, 10):  # increment of +1 is implied
    print(x)

for x in range(10):	# increment of +1 and start at 0 is implied
    print (x)

for x in range(5, 1, -3):
    print(x)

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
for v in my_list:
    print(v)

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keys
#for key in capitals.keys():
    #print(key)
#to iterate through the values
#for val in capitals.values():
    #print(val)
#to iterate through both keys and values
#for key, val in capitals.items():
    #print(key, " = ", val)

#While loops
for count in range(0,5):
    print("looping = ", count)

count = 0
while count < 5:
    print("looping  ", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1