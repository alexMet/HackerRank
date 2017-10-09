ar = [int(i) for i in input().split()]

fir = ar[0]
sec = ar[1]
n = ar[2]

for _ in range(0, n-2):
    temp = sec**2 + fir
    fir = sec
    sec = temp
    
print(sec)
