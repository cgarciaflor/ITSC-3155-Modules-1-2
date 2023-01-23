number_array = []
number2_array = []
counter = 0
counter2 = 0

while counter < 5:
    num = int(input("Input a number for the first list: "))
    number_array.append(num)
    counter += 1

while counter2 < 5:
    num = int(input("Input a number for the second list: "))
    number2_array.append(num)
    counter2 += 1

print("First List: ", number_array)
print("Second List: ",number2_array)
common_list = set(number_array).intersection(number2_array)
print("Common List: ", common_list)
