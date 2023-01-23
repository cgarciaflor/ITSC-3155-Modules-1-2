string = input("Enter a string: ")

new = string.replace(" ", "")

lower = []
upper = []

for char in new:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

str = ''.join(lower + upper)
print(str)