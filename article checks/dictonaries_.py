myDict = {}  # empty dictionary
print(myDict)
myDict = {"key": "value", 1: "kenya", 2: "uganda"}  # with values
print(myDict)
myDict[1] = " Nigeria"  # access the key and give new  value
print(myDict)
myDict[3] = "Niger"  # adding a new key value pair
print(myDict)

myDict = {'key': 'value', 1: ' Nigeria', 2: 'uganda', 3: 'Niger'}
x = myDict.pop(3)  # pop element
print(x)
print(myDict)
y = myDict.popitem()  # empty dictionary
print(y)
print(myDict)
myDict.clear()
print(myDict)

myDict = {'key': 'value', 1: ' Nigeria', 2: 'uganda', 3: 'Niger'}
print(myDict[1])  # access elements using keys
print(myDict.get(3))  # access using get()

myDict = {'key': 'value', 1: ' Nigeria', 2: 'uganda', 3: 'Niger'}
print(myDict.keys())  # get keys
print(myDict.values())  # get values
print(myDict.items())  # get key-value pairs
