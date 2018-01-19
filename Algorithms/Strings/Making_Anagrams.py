st1 = input()
st2 = input()

l1 = len(st1)
l2 = len(st2)

a1 = [0]*26
a2 = [0]*26

for i in range(l1):
    a1[ord(st1[i]) - 97] += 1

for i in range(l2):
    a2[ord(st2[i]) - 97] += 1

cnt1 = 0
for i in range(26):
        cnt1 += abs(a1[i] - a2[i])
        
print (cnt1)
