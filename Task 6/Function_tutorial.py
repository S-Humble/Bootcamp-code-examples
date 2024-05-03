#with parameter and return statement

def add(num1, num2) : #paramemters
    """This function returns the sum pf num1 and num2"""
    return num1 + num2

sum_value = add (10, 20)
print (sum_value)
print (add(20,30))

#without paramemter
def greet():
    print ("Hi my name is Sam.")

greet()

#with parameter
def greet_1(a):
    print (f"Hi my name is {a}")

greet_1("Spongebob")

#f ~ string input built in function 
random_text = input("What is your favourite food?")
print (f"We are out of {random_text}.")

print (f"Length of user input: {len(random_text)} \n Sorry that you can't eat {random_text} today.") # \n Print on new line 

#random function 
def hogwarts (h1, h2):
    print (f"Character 1 {h1} \n character 2: {h2}")
    print (f"You have an extra chaaracter: {global_h}")

global_h = "Hermione" #global variable - needed before function call 
hogwarts ("Harry", "Ron")


def my_func():
    global y #makes y into global variable whilst in function
    y = "Here comes the sun"
    print (y)

my_func()
print(y)