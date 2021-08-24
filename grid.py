number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][1]) #outpt=2


for row in number_grid:
    print(row)

numbers = [10,20,30,40,50]
print(numbers)

numbers[1]= 29
print(numbers)
print(numbers[0])

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(numbers[i])

print(numbers[0:-2]) #output=[10,29, 30]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)

def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))