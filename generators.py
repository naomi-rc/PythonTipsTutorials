# generators are iterators that can only be iterated over once
# They are implemented as functions that yield a value (not return)
# next(generator) returns the next element in the sequence or StopIteration error
# iter(iterable) returns the iterable's iterator

def my_generator(x):
    for i in range(x):
        yield i

print(next(my_generator(10)))

print()

for i in my_generator(10):
    print(i)

print()
try: 
    my_string = "Hi"
    iterator = iter(my_string)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except:
    print("No more elements left - Threw a StopIteration exception as expected")
