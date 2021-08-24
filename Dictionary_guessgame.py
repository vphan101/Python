monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Jan"])
print(monthConversions.get("Jan"))


#while Loop

i = 1
while i <= 10:
    print(i)
    i +=1

print("Done with loop because i is 11")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:

        guess = input("Enter guess(you have 4 guesses):")
        guess_count +=1
        out_of_guesses = False

    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, you lose")
else:
    print("You guessed the correct secret word within 4 guesses")


for letter in "Giraffe Academy":
    print(letter)