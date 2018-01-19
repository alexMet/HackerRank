def cnt_digi(digit, n):
    cnt = 0
    
    for i in range(len(digit)):
        d = int(digit[i])
        if d == 0:
            continue
           
        if not (n % int(digit[i])):
            cnt += 1
            
    return cnt

t = int(input())

for _ in range(t):
    line = input()
    print (cnt_digi(line, int(line)))
