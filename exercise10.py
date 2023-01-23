String = input("Enter a string: ")
charList = [*String]
print(charList)
start = 0
end = len(charList)
size = 3
x = [charList[i:i + size] for i in range(0, len(charList), size)]
print(x)