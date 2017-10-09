t = int(input())
glo = [0]*26

for i in range(0, t):
    string = input()
    
    a = [0]*26
    for l in string:
        a[ord(l) - 97] += 1
    
    for l in range(0, 26):
        if a[l] > 0:
            glo[l] += 1
            
cnt = 0
for i in glo:
    if i == t:
        cnt += 1
        
print (cnt)
