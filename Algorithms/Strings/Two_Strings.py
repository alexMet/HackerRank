def tsouki():
    a = input()
    b = input()
    
    for l in a:
        if l in b:
            return "YES"
    return "NO"

n = int(input())

for _ in range(0, n):
    print (tsouki())
