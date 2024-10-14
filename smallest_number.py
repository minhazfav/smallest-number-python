a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
c = int(input('Enter the third number'))

smallest = 0

if a < b and a < c : 
    smallest = a

if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c


print(smallest, 'is the smallest number among those three')


