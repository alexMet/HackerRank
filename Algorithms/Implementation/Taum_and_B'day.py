t = int(input())

for _ in range(t):
    line = input().split()
    b,w = list(map(int, line))
    
    line = input().split()
    x,y,z = list(map(int, line))
    
    print (min([b*x+w*y, b*x+w*(x+z), b*(y+z)+w*y]))
