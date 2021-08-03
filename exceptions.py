# exceptions mechanisms : try, except (one at a time, multiple at a time, all), finally, else
# (consider each except clause separately)

try:
    print("This is what we want to try without errors")
    # raise IOError
    # raise KeyError
    # raise NameError
    # raise TypeError
    # raise ValueError
except IOError:
    print("This prints if there is an IOError")
except KeyError:
    print("This prints if there is a KeyError")
except (NameError, TypeError) as e:
    print("This prints if there is an NameError or a TypeError")
except Exception as e:
    print("This prints if there is any type of exception")
except:
    print("This also prints if there is any type of exception")
else:
    print("This prints if there is no exception")
finally:
    print("This prints whether there is an exception or not")

