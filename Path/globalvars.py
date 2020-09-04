# if we have variables created outside a function 
# we can access them inside a function but you can't change them.

rocketText = 'We will launch in '

# def OutPutRocketText():
#     This will throw an error
#     rocketText = rocketText + 'two days'
#     return

# To solve this we have two options
# Make a variable a global variable
# Give a variable to the function, so it knows what the variable is and then return it

# make a global var
def OutPutRocketText():
    global rocketText
    rocketText = rocketText + 'two days'
    return rocketText

OutPutRocketText()
print(rocketText)

# Another way to modify variables inside a function
# is to use parameters

def rocketLaunch(text_input):
    text_input = text_input + 'three days'
    return text_input

textinput = 'the rocket will launch in '
new_rocket = rocketLaunch(textinput)
print(new_rocket)