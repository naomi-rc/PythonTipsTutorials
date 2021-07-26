# Ternerary operator: short hand if else statement : value_if_true if condition else value_if_false or (if_test_is_false, if_test_is_true)[test]

value = "I evaluate to True" if 7 > 5 else "I evaluate to False"
print(value)

#not recommended as it is not pythonic and easy to confuse where to put True/False values
value = ("But I evaluate to False","I also evaluate to True")[2 > 5] 
print(value)

