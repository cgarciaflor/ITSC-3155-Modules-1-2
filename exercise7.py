i = [] 
n = []
while True: 
    inp = input("Enter a number or QUIT to quit: ") 
    if inp == 'QUIT': 
        break 
    i.append(int(inp)) 
    if(int(inp)%2 == 0):
        n.append(int(inp))
print("All nums: ", i) 
print("Even nums", n)