#Method one
language = 'Python'
lst = list[language]
print(type(lst))
print(lst)

#Second one using list comprehension 
lst = [i for i in language]
#print(type(lst))
print(lst)

#Generating numbers
numbers = [i for i in range(100)]
print(numbers)

#We can do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)

sum = [i + i for i in range(10)]
print(sum)

#We can also make list of tuples 
numbers = [(i,i + i) for i in range (11)]
print(numbers)
#List Comprehension can be combined with if expression
#Generating even numbers
even_numbers = [i for i in range (21) if i % 2 == 0]
print(even_numbers)

#Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

#Filtering out positive integers
num = [-1,-2,-3,4,-5,2,3,4,6,-10,30,-1,-8,12,14]
pos_num = [i for i in num if i > 0]
print(pos_num)

#Filtering out positive and even numbers
num = [-1,-2,-3,4,-5,2,3,4,6,-10,30,-1,-8,12,14]
pos_even_num = [i for i in range(30) if i % 2 == 0 and i > 0]
print(pos_even_num)

#Flattening a three dimensional array
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

#Lambda Function
#Named Function
def add_two_numbers(x,y):
    return x + y
print(add_two_numbers(9,2))

#above function can be changed to a lambda funtion
add_two_numbers = lambda x, y : x + y
print(add_two_numbers(2,4))

#self invoking lambda funtion
print((lambda x, y: x + y)(2,5))

square = lambda x: x ** 2
print(square(3))

cube = lambda x: x ** 3
print(cube(3))

mult_var = lambda a, b, c: 2 * a + 4 * b + 6 * c
print(mult_var(1,2,3)) 

#Lambda Function inside another function
def power(a):
    return lambda b: a ** b
cube = power(2)(3)
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)
print(power(2)(5))

#Exercise

#1
numbers = [-4,-3,-2,-1,0,2,4,6]
neg_zero_num = [i for i in numbers if i < 0 or i == 0]
print(neg_zero_num)

#2
list_of_lists = [[[1,2,3]],[[4,5,6]],[[7,8,9]]]
flattened_lists = [number for row in list_of_lists for number in row]
print(flattened_lists)

#3
#numbers = 1
num_1 = [0 ** i for i in range(6)]
t_num_1 = tuple(num_1)
#print(num_2)

num_2 = [1 ** i for i in range(6)]
t_num_2 = tuple(num_2)

num_3 = [2 ** i for i in range(6)]
t_num_3 = tuple(num_3)
#print(num_3)

num_4 = [3 ** i for i in range(6)]
t_num_4 = tuple(num_4)
#print(num_4)

num_5 = [4 ** i for i in range(6)]
t_num_5 = tuple(num_5)
#print(num_5)

num_6 = [5 ** i for i in range(6)]
t_num_6 = tuple(num_6)
#print(num_6)

num_7 = [6 ** i for i in range(6)]
t_num_7 = tuple(num_7)
#print(num_7)

num_8 = [7 ** i for i in range(6)]
t_num_8 = tuple(num_8)
#print(num_8)

num_9 = [8 ** i for i in range(6)]
t_num_9 = tuple(num_9)
#print(num_9)

num_10 = [9 ** i for i in range(6)]
t_num_10 = tuple(num_10)
#print(num_10)

num_11 = [10 ** i for i in range(6)]
t_num_11 = tuple(num_11)
#print(num_11)

list = [t_num_1, t_num_2, t_num_3, t_num_4, t_num_5, t_num_6, t_num_7, t_num_8, t_num_9, t_num_10, t_num_11]
print(list)

#4
countries = [[('Finland','Helsinki')],[('Sweden','Stockholm')],[('Norway','Oslo')]]
Countries_new_list = [countries for row in countries for countries in row]
#Countries_new_list_cap = Countries_new_list.upper()
print(Countries_new_list)

#7
#a1 = input('Enter a1: ')
#a2 = input('Enter a2: ')
#b1 = input('Enter b1: ')
#b2 = input('Enter b2: ')
m = lambda  a1, a2, b1, b2 : (b2 - b1) / (a2 - a1) 
#print('The slope of {},{},{},{} is: '.format(a1,a2,b1,b2), m)
print(m(1,2,3,4))
