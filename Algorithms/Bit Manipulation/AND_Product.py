n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    list_a = []
    list_b = []
    list_c = []
    
    for i in range(32):
        list_a += str(a & 0x1)
        list_b += str(b & 0x1)
        a >>= 1
        b >>= 1
        
    list_a.reverse()
    list_b.reverse()
        
    cut = 0
    for i in range(32):
        if (list_a[i] != list_b[i]):
            cut = i
            break
        
        list_c += [list_b[i]]
        
    print (int("".join(list_c + ['0']*(32 - cut)), 2))
