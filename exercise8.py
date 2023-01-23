i = []
t = []
b = 1
count = 0
while count < 10:
    print("Enter number ", b, ':')
    num = int(input())
    i.append(num)
    count+=1
    b+=1
print("Original List: ", i)
one = [c for c in i if i.count(c) < 2]
print("Only Once: ", one)
