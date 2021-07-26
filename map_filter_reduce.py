from functools import reduce

#map: map(function, values)
def my_map(values):
    times_three = map(lambda x: x*3, values)
    return list(times_three)

#filter: filter(function, values)
def my_filter(values):
    even_digits = filter(lambda x: x%2==0, values)
    return list(even_digits)

#reduce: reduce(function, values) - applies a rolling computation to sequential pairs of values in a list
def my_reduce(values):
    sum_of_all = reduce(lambda x, y: x + y, values)
    return sum_of_all
    #return list(sum_of_all)

values = [1,2,3,4,5]
print(f"Values: {values}")
print(f"My map result: {my_map(values)}")
print(f"My filter result: {my_filter(values)}")
print(f"My reduce result: {my_reduce(values)}")
