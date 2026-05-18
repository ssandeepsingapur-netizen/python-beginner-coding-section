n = int(input("enter number items "))
dict = {}
for i in range(n):
    key = input("enter the key: ")
    value = input("enter the value: ")
    dict[key] = value
print("the dictionary is:", dict)
print("the keys in the dictionary are:", dict.keys())
print("the values in the dictionary are:", dict.values())
print("the items in the dictionary are:", dict.items())
key_to_remove = input("enter the key to remove: ")
if key_to_remove in dict:
    del dict[key_to_remove]
    print("the dictionary after removing the key is:", dict)
else:    print("the key is not found in the dictionary")
key_to_update = input("enter the key to update: ")
if key_to_update in dict:
    new_value = input("enter the new value: ")
    dict[key_to_update] = new_value
    print("the dictionary after updating the key is:", dict)
else:    print("the key is not found in the dictionary")
