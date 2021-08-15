# slots : mechanism that tells Python to allocate only a fixed/static set of attributes 
# upon object creation instead of storing a dictionary which wasted a lot of RAM

class MyRegularObject(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class MySlotsObject(object):
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age