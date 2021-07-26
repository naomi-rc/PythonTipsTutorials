#Set: data structure for list of unique values

list = [1,2,3,4,2,3]
print(f"The list: {list}")
print(f"The unique values: {set(list)}")
print(f"The duplicates: {set([x for x in list if list.count(x) > 1])}")

print(f"\nThis is also a set (duplicated are automatically removed): {1,2,3,4,2,3}")

set_a = {1,2,3,4,5}
set_b = {3,4,5,6,7}

print(f"\nThe sets : {set_a} and {set_b}")
print(f"Intersection: {set_a.intersection(set_b)}")
print(f"Difference (set_a - set_b): {set_a.difference(set_b)}")
print(f"Difference (set_b - set_a): {set_b.difference(set_a)}")