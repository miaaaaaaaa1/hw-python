#1

try:
    number = int(input("Enter the number: "))
    if number < 0:
        raise ValueError("A negative number does not have a real square root")
    sqrt = number*number
    print(sqrt)
except ValueError:
    print()

#3

myDict = {"Key1" : "Value1" , "Key2" : "Value2"}
def menu():
  print("1. Show dict")
  print("2. Search value dict")
  print("3. Replace mean")
  print("4. Show by key")
  print("5. Delete by key")
  return int(input("Enter your choice : "))
                 
def showDict(dictinary):
 for key, value in dictinary.items:
  print(f"Key: {key} value : (value)")
choice = menu

def searchValue(dictionary):
    value = input("Enter a value to search for: ")
    found_keys = [key for key, val in dictionary.items() if val == value]
    if found_keys:
     print(f"Value '{value}' found for keys: {found_keys}")
    else:
     print(f"The value '{value}' was not found in the dictionary.")


def replaceValue(dictionary):
    key = input("Enter the key to replace the value: ")
    if key in dictionary:
        new_value = input("Enter a new value: ")
        dictionary[key] = new_value
        print(f"The value for the key '{key}' changed to '{new_value}'")
    else:
        print(f"Key '{key}' not found in the dictionary.")

def showValue(myDict):
  key = input("Enter key: ")
  if key in myDict:
    print(f"Value : {myDict[key]}")
  else:
    print("Invalid key")

def deleteValue(dictionary):
 key = input("Enter the key to delete: ")
 if key in dictionary:
   del dictionary[key]
   print(f"Value for key '{key}' deleted")
 else:
  print("Invalid key")

match choice:
 case 1:
  showDict(myDict)
 case 2:
  searchValue(myDict)
 case 3:
  replaceValue(myDict)
 case 4:
  showValue(myDict)
 case 5:
  deleteValue(myDict)
