#decorators : functions that modify the functionality of other functions

from functools import wraps

# 1. Everything in python is an object - functions are assigned as variables
# 2. Functions can be nested (not accessible outside of those functions - unless returned)
# 3. Functions can return functions
# 4. Functions can be passed as arguments ( do something in functions a before executing b by doing a(b) )
# 5. @a_new_decorator is short for a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# 6. Use functools.wraps to access the properties of overridden functions - use it as a decorator @wraps before returning wrapped function
# Use cases: authorization (wrap function requiring authorization), logging

# 1. Everything in python is an object - functions are assigned as variables
def function_b():
    return "hello world"

function_a = function_b

print(function_a) # <function function_b at 0x00000167F17FF040>
print(function_a()) #hello world


# 2. Functions can be nested (not accessible outside of those functions - unless returned)
# 3. Functions can return functions
def function_c():
    def nested_function():
        return "I am a nested function"
    return nested_function

print(function_c) # <function function_c at 0x000001382DAEC700>
print(function_c()) # <function function_c.<locals>.nested_function at 0x000001382DAEC790>
print(function_c()()) # I am a nested function


# 4. Functions can be passed as arguments ( do something in functions a before executing b by doing a(b) )
def passed_function():
    return "I am a passed function"

def function_d(function):
    print(function)
    print(function())

function_d(passed_function) # <function passed_function at 0x000002DE1D6DC8B0>
                            # I am a passed function


# 5. @a_new_decorator is short for a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
def decorate_function(function):
    def decorated_function():
        print("Did something before")
        print(function())
        print("Did something after")
    return decorated_function

def function_to_be_decorated():
    return "I am the function to be decorated"

function_to_be_decorated = decorate_function(function_to_be_decorated)

function_to_be_decorated() 
# Did something before
# I am the function to be decorated
# Did something after

## NOW WITH DECORATOR SHORT HAND ##
def decorate_function(function):
    def decorated_function():
        print("Did something before")
        print(function())
        print("Did something after")
    return decorated_function

@decorate_function
def function_to_be_decorated():
    return "I am the function to be decorated"

function_to_be_decorated() 
# Did something before
# I am the function to be decorated
# Did something after

# 6. Use functools.wraps to access the properties of overridden functions - use it as a decorator @wraps before returning wrapped function
def decorate_function(function):
    def decorated_function():
        print("Did something before")
        print(function())
        print("Did something after")
    return decorated_function

@decorate_function
def function_to_be_decorated():
    return "I am the function to be decorated"

print(f"Function name: {function_to_be_decorated.__name__}") #Function name: decorated_function

## NOW WITH FUNCTOOLS.WRAPS ##
def decorate_function(function):
    @wraps(function)

    def decorated_function():
        print("Did something before")
        print(function())
        print("Did something after")
    return decorated_function

@decorate_function
def function_to_be_decorated():
    return "I am the function to be decorated"

print(f"Function name: {function_to_be_decorated.__name__}") # Function name: function_to_be_decorated