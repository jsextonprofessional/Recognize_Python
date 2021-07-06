num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, string, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, number, string, boolean, initialize list
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, string, initialize list
print(type(fruit)) # log statement
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') #string
print(person['name']) # log statement, string
person['name'] = 'George' # variable declaration, string, initialize list
person['eye_color'] = 'blue' # variable declaration, string, initialize list
print(fruit[2]) # log statement

if num1 > 45: # number
    print("It's greater") # log statement, string
else:
    print("It's lower") # log statement, string

if len(string) < 5: # length check, number
    print("It's a short word!") # log statement, string
elif len(string) > 15: # length check, number
    print("It's a long word!") # log statement, string
else:
    print("Just right!") # log statement, string

for x in range(5): # number
    print(x) # log statement
for x in range(2,5): # number
    print(x) # log statement
for x in range(2,10,3): # number
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # number
    print(x) # log statement
    x += 1 # variable declaration, number

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) # log statement
person.pop('eye_color') # string
print(person) # log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni': # boolean
        continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # boolean
        break

def print_hello_ten_times():
    for num in range(10): # number
        print('Hello') # log statement, string

print_hello_ten_times() # log statement

def print_hello_x_times(x): # log statement
    for num in range(x):
        print('Hello') # log statement, string

print_hello_x_times(4) # log statement, number

def print_hello_x_or_ten_times(x = 10): # log statement, number
    for num in range(x):
        print('Hello') # log statement, string

print_hello_x_or_ten_times() # log statement
print_hello_x_or_ten_times(4) # log statement, number

#multiline comment
"""
Bonus section 
"""
#single line comments
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)