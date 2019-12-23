# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 01:43:44 2019

@author: Osheen
"""
for i in range(1,5):
    print(i)
    
squares=[]
for i in range(1,11):
    square = i**2
    squares.append(square)
print(squares)


random=[]
for i in range(12,21):
      div=i/2
      random.append(div)
print(random)   


#CHAPTER 4**********************************************************8
for i in range(1,21):
    print(i)
    '
list=[]
for i in range(1,10000001):
    value=i
    list.append(value)
print(list)
    
million=[i for i in range(1,1000001)]
min(million)
max(million)
sum(million)

#odd_number= list(range(1,20,2))
#rint(odd_number)

#even_numbers = list(range(2,11,2)) 
#print(even_numbers)

odd =[]
for i in range(1,21):
    v=i+2
    odd.append(v)
print(odd)

multiple =[]
for i in range(3,31):
    v=i*3
    multiple.append(v)
print(multiple)


cubes =[]
for i in range(1,11):
    v=i**3
    cubes.append(v)
print(cubes)

cubes=[i**3 for i in range(1,11)]
print(cubes)


no =[ 1,2,3,4,5,6,7,8,9,10]

print("The first three numbers are:")
print(no[:3])
print("\nThe middle four numbers are:")
print(no[3:7])
print("The first three numbers are:")
print(no[-3:])




my_pizza = ['pep', 'beef', 'veg', 'mix', 'alll']
friend_pizza= my_pizza[:]
my_pizza.append('real')
print(my_pizza)
friend_pizza.append('dare')
print("My favorite pizza are")
for i in my_pizza:
    print(i)
print("\nMy friends favorite pizza are")
for i in friend_pizza:
    print(i)


menu=('chicken','beef','pork')
print("The old menu")
for i in menu:
    print(i)

menu=('duck','salmon','chicken')
print("New menu")
for i in menu:
    print(i)
    
