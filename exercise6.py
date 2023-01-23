T = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

i = int(input("Enter a row num from 1 to 5: "))
n = int(input("Enter a col num from 1 to 5: "))

T[i-1][n-1] = 1
for r in T:
   for c in r:
      print(c,end = " ")
   print() 