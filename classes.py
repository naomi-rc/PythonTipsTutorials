# class variable vs instance variables
    # class variables are shared by different instances of a class
    # instance variables are unique to a single instance or object of a class
    # avoid using mutable classes variables unless necessary

class MyClass():
    class_variable = "I am a class variable"

    def __init__(self):
        self.instance_variable = "I am an instance variable"

myObject = MyClass()
print(myObject.class_variable)
print(myObject.instance_variable)


# old classes vs new classes
    # new classes inherit from object while old classes do not (except in Python 3 where they always do)
class OldClass():
    def __init__(self):
        print("I am an old class")

class NewClass(object):
    def __init__(self):
        print("I am a new class")


# magic methods (init and getitem)
class CountryLanguage():
    def __init__(self):
        self.items = {"russia": "russian", "spain": "spanish", "china": "chinese"}
    
    def __getitem__(self, value):
        return self.items[value]

countryLanguage = CountryLanguage()
print(countryLanguage["spain"])