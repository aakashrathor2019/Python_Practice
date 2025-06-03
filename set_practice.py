#Set Exmaples
set1 = {1, 2, 3}
set2 = set([3, 4, 5])
print(set1) 
print(set2) 

#Uniion of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set1 = set1 | set2
union_set2 = set1.union(set2)
print(union_set1) # Output: {1, 2, 3, 4, 5}
print(union_set2) # Output: {1, 2, 3, 4, 5}

#Intersection of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set1 = set1 & set2
intersection_set2 = set1.intersection(set2)
print(intersection_set1) # Output: {3}
print(intersection_set2) # Output: {3}

#Difference of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set1 = set1 - set2
difference_set2 = set1.difference(set2)
print(difference_set1) # Output: {1, 2}
print(difference_set2) # Output: {1, 2}

#Symmetric Difference of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set1 = set1 ^ set2
symmetric_difference_set2 = set1.symmetric_difference(set2)
print(symmetric_difference_set1) # Output: {1, 2, 4, 5}
print(symmetric_difference_set2) # Output: {1, 2, 4, 5}

#Subset and Superset
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2)) # Output: True
print(set2.issuperset(set1)) # Output: True


#Add and Remove Elements
set1 = {1, 2, 3}
set1.add(4)
print(set1) # Output: {1, 2, 3, 4}
set1.remove(4)
print(set1) # Output: {1, 2, 3}
set1.discard(5) # does not raise an error if element is not present
print(set1) # Output: {1, 2, 3}