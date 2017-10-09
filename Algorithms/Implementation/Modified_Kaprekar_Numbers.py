n = int(input())
m = int(input())

ans = []
for i in range(n, m + 1):
    si = str(i)
    sil = len(si)
        
    ss = str(i * i)
    ssl = len(ss)
        
    if ssl == 1:
        if ss == si:
            ans += [si]
    else:
        if ssl % 2 == 0:
            if int(ss[sil:]) + int(ss[:sil]) == i:
                ans += [si]
        else:
            if int(ss[sil - 1:]) + int(ss[:sil - 1]) == i:
                ans += [si]
        
if not ans:
    print ("INVALID RANGE")
else:
    print (' '.join(ans))
