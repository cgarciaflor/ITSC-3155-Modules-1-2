counter = 0
number_array = []

b = int(input("Enter a number:"))

while counter < b:
    num = float(input("Input a number: "))
    number_array.append(num)
    counter += 1

total = 0

for number in number_array:
    total = total + number

average = total / b
print(number_array)
print("The average is ", average)