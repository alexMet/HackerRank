def is_pali(st, left, right):
    l = right - left + 1
    
    for i in range(l):
        if st[left + i] != st[right - i]:
            return False
        
    return True
    
def rem(st):
    l = len(st)

    k = -1
    for i in range(l//2):
        if st[i] != st[l-i-1]:
            k = i
            break
            
    if k != -1:
        if is_pali(st, k, l-k-2):
            return l-k-1
        else:
            return k
        
    return k
            

t = int(input())

for _ in range(t):
    print (rem(input()))
