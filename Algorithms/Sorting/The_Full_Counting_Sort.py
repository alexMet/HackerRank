n = int(input())
cnt = [0] * 100

dat = {}
for i in range(0, 100):
    dat[i] = []

for i in range(0, n):
    num, st = input().split()
    num = int(num)
    
    cnt[num] += 1
    dat[num] += [st] if i >= n / 2 else ['-']
    
ans = ""
for i in range(0, 100):
    ans += ' '.join(dat[i]) + ' '

print (ans)
