n = int(input())
st = input()
key = int(input())

st = list(map(ord, st))

for i in range(0, len(st)):
    l = st[i]
    if l >= 97 and l <= 122:
        st[i] = (l-97+key)%26 + 97
    if l >= 65 and l <= 90:
        st[i] = (l-65+key)%26 + 65
    
print ("".join(list(map(chr, st))))
