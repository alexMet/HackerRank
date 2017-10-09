n = int(input())
ar1 = list(map(int, input().split()))
m = int(input())
ar2 = list(map(int, input().split()))

dic1 = {}
for i in ar1:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 0
        
dic2= {}
for i in ar2:
    if i in dic2:
        dic2[i] += 1
    else:
        dic2[i] = 0

dic3 = []
for i in dic1.keys():
    if i in dic2:
        if dic1[i] != dic2[i]:
            if i not in dic3:
                dic3.append(i)
    else:
        if i not in dic3:
            dic3.append(i)
            
dic3.sort()
print (" ".join(list(map(str, dic3))))
