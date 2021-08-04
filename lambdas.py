# lambdas : one-line, anonymous functions

power = lambda x, y : x ** y
print(power(5, 2))

my_dictionary = {'a': 1, 'b': 2, 'c':3, 'A': 27, 'B': 28, 'C': 29}
swapper = lambda dictionary: {value : key for key, value in dictionary.items()}
print(swapper(my_dictionary))


nums_in_range_divisible_by = lambda r, d: [x for x in range(r) if x%d==0]
print(nums_in_range_divisible_by(10, 3))