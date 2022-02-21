mySet={1,4,5,7,8,8,9,1,1}
print(mySet)

mySet={1,4,5,7,8,8,9,1,1}
mySet.add("string ")
print(mySet)

mySet = {1, 2, 3, 4}
mySet_2 = {3, 4, 5, 6}
print(mySet.union(mySet_2), '==', mySet | mySet_2) # union() function combines the data present in both sets.
print(mySet.intersection(mySet_2), '==', mySet & mySet_2) # intersection() function finds the data present in both sets only
print(mySet.difference(mySet_2), '==', mySet - mySet_2)  # difference() function deletes the data present in both and outputs data present only in the set passed.
print(mySet.symmetric_difference(mySet_2), '==', mySet ^ mySet_2) # symmetric_difference() does the same as the difference() function but outputs the data which is remaining in both sets.
mySet.clear()
print(mySet)

