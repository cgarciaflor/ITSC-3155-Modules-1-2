num = int(input("Enter a number between 0 - 100: "))

if(num <= 100 & num >= 90):
    print("Your grade is an A")
elif(num <= 89 & num >= 80):
    print("Your grade is a B")
elif( num <= 79  & num >= 70):
    print("Your grade is a C")
elif( num <= 69  & num >= 60):
    print("Your grade is a D")
else:
    print("Your grade is a F")



