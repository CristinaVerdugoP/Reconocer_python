#variable declaration:
num1 = 42 # - Data Types: Numbers
num2 = 2.3 # - Data Types: Numbers
boolean = True # - Data Types: Numbers
string = 'Hello World' # Data Types: Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # inicializar lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #inicializar dictionary
fruit = ('blueberry', 'strawberry', 'banana') #inicializar tupla
#--------------------------------------------------------
print(type(fruit)) # - type check
print(pizza_toppings[1]) # List: out ()
pizza_toppings.append('Mushrooms') # List: add value
print(person['name']) # Dictionary: access value
person['name'] = 'George' # Dictionary: change value
person['eye_color'] = 'blue'# Dictionary: add value
print(fruit[2]) # Tuple: access value

if num1 > 45: #Conditional: if-else
    print("It's greater")
else:
    print("It's lower")
#------------------------------------------
if len(string) < 5: #Conditional: if-elif-else
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#-------------------------------------------
for x in range(5): #for loop: start (los tres devuelven una lista)
    print(x) #stop
for x in range(2,5):#for loop: start
    print(x)#stop
for x in range(2,10,3):#for loop: start
    print(x)#stop
#-------------------------------------------
x = 0 #variable declaration
#start while loop
while(x < 5): #Cuando llegue a 4: stop
    print(x)
    x += 1 #increment 

 
pizza_toppings.pop() # List : Remove
pizza_toppings.pop(1) #Remove

print(person) #acces value
person.pop('eye_color') #remove
print(person) #acces value

for topping in pizza_toppings: #start for loop
    if topping == 'Pepperoni': #start conditional if
        continue 
    print('After 1st if statement') 
    if topping == 'Olives': 
        break #stop for loop

def print_hello_ten_times(): # function declaration
    #parameters
    for num in range(10): #for loop
        print('Hello')

print_hello_ten_times() #return function (?)

def print_hello_x_times(x): # function declaration
    #parameters x
    for num in range(x): #for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # function declaration
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

print(num3) #deberia dar un error: NameError: name <variable name> is not defined
num3 = 72 #Declarate value
fruit[0] = 'cranberry'
print(person['favorite_team']) #KeyError: 'favorite_team'
print(pizza_toppings[7])
print(boolean)
fruit.append('raspberry') #deberia dar un error, ya que la tupla no se modifica:- AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #deberia dar un error ya que se quiere aliminar algo a una tupla: - AttributeError: 'tuple' object has no attribute 'pop'