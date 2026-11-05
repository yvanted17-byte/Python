#I create a variable containing Nba players
'''
first_name = 'Ja Morant'
Team = 'Portland'
Jeysey_nummber = 12
Partner = 'Nike'
Major_skills = {'high jump', 'Spectaculous Dunk', 'speed', 'Dribble'}
Origin = 'US'

print(len(Major_skills))
'''
#Now i try printing out the invidial results
'''print('First name:', first_name)
print('Team:', Team)
'''
#how to change dat types
'''x_int=10
print('integer:',x_int)
float_x= float(x_int)
print('decimal of x= ', float_x)

a=12
print('int_a= ', a)
m= str(a)
print('string of a=', m)
'''
#day 3: Booleans
'''
print(True)
print(False)
'''
#operations
# Arithmetic Operations in Python
# Integers
'''
print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2
print(len('python')==len('dragon'))
age=int()
print('write your age')
age=input(age)

print('your age is: ', age)
'''
#day 4: Strings
'''
first_name= 'me'
print(len(first_name))
#because first name is me which has 2 characters
#concatenation of strings:
first_name= 'ja'
last_name= 'morant'
full_name= first_name + last_name
print(full_name)
print(len(full_name))

\n new line
\t space out 8
\\ back slash
\' single quote
\" double quote
'''
#styling string
'''
first_name = 'Ja Morant'
Team = 'Portland'
Jeysey_nummber = 12
Partner = 'Nike'
player='I am {} i play for {} as number {}. I do be a parthner for {}'.format(first_name, Team,Jeysey_nummber,Partner)
print(player)
'''
# let's do a program which calculates the area of a circle from the diameter
'''
print('Enter the radius of the circle:')

a=int(input('Enter the radius of the circle:'))
area=3.14*(a**2)
print('the area is:', area)
'''
#String with index
first_name= 'Morant'
print('the name is :', first_name)
inversed_form= first_name[::-1]
'''print(inversed_form)
print (inversed_form[0])
print(inversed_form[1:5]) '''#it doest show the 5th element. it takes value from the 2nd to the 4th


#challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
'''.count('element') to count the number of times a character appears in a string
.endswith('element or character') to check if the elemnt ends with a given character or characters
.expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
.find(): Returns the index of the first occurrence of a substring, if not found returns -1'''

#day 5: List
#Positiv indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
