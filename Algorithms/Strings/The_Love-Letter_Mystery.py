def make_it_pali(st):
    l = len(st)
    cnt = 0
    
    for i in range(l // 2):
        if st[i] != st[l-i-1]:
            cnt += abs(ord(st[i]) - ord(st[l-i-1]))

    return cnt

t = int(input())

for _ in range(t):
    print (make_it_pali(input()))
