for x in range(0,10,1):
    print (x)

for x in range(5,25,5):
    print(x)

for x in range(1,20):
    if x/5:
        print('Coding')
    if x/10:
        print('Coding Dojo')

sum=0
for x in range(0,10):
    if x%2==1:
        sum= sum +x
    print(sum)

for x in range(100,0,-4):
    print(x)

for x in range(2,10,1):
    if x%3==0:
        print(x)

def square_numbers(num):
    result = [ ]
    for i in num:
        result.append(i*i)
    return result

my_num = square_numbers([1,2,3,4,5])
print(my_num)