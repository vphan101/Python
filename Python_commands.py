numbers = [2,4,6,8,10]
friends = ["Kevin", "Vinh","Mike","Jim"]
phrase = "Giraffe Academy"

print(phrase.replace("Giraffe", "Elephant"))

print(friends[0])
print(friends)
print(friends[1:3]) #["Vinh","Jim"]
friends[1]="You"
print(friends)

friends.extend(numbers)
print(friends) #["Kevin","You","Mike","Jim",2,4,6,8,10]

friends.insert(1,"Me")
print(friends) #["Kevin","You", "Me", .......`10]

friends.reverse()
print(friends)  #[10,8,6,....."Kevin"]

friends.remove("Me")
print(friends)
#friends.clear()
#print(friends) will clear everything  = []


print(friends.index("Mike"))

friends2 =friends.copy()
print(friends2)

