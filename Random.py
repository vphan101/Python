import random
import string

print(random.randrange(0,200))


greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']

value = random.choice(greetings)
print(value)

def random_string(length=32):
    character_set = string.ascii_letters
    return ''.join(random.choice(character_set) for i in range(length))

my_random = random_string(10)
print(my_random)


movies = ['Star Wars', "Ghandi", "Casablanca", "Gone with the Wind", "Citizen Kane",
"Gataca", "Ghostbusters", "2001", "Raiders of the Lost Ark"]

gmovies = [ ]
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)
