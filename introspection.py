# dir : functions and attributes belonging to an object 
print(f"{dir(list)}\n")

# type : returns type of object
print(f"{type('hi')}\n")

# id : returns unique identification of an object
print(f"{id('hi')}\n") # will be different each time

# inspect module : provides other functions for introspection (more info than dir)
import inspect
print(f"{dir(str)}\n")
print(inspect.getmembers(str))


