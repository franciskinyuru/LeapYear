myList = [] # create empty list
print(myList)
myList = [1,3,"john"] #creating list with data

myList = [1,3,"john"]
print(myList)
myList.append(4) #add as a single element
print(myList)
myList.extend([10, 'more_example']) #add as different elements
print(myList)
myList.insert(3, 'insert_example') #add element i given position
print(myList)
myList=[1, 3, 'insert_example', 4, 10, 'more_example']
del myList[2] #delete element at index 2
print(myList)
myList.remove('more_example') #remove element with value
print(myList)
a = myList.pop(1) #pop element from list
print('Popped Element: ', a, ' List remaining: ', myList)
myList.clear() #empty the list
print(myList)


print("############################")

myList = [1, 2, 3, 'john', 10, 15]
for element in myList: #access elements one by one
    print(element)
print(myList) #access all elements
print(myList[4]) #access index 4 element
print(myList[0:2]) #access elements from 0 to 1 and exclude 2
print(myList[::-1]) #access elements in reverse