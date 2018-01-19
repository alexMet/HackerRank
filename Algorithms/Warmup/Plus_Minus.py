n = int(raw_input())
a = map(int, raw_input().split())
pos = neg = zer = 0

for i in range(0, n):
    if a[i] < 0:
        neg+=1
    if a[i] > 0:
        pos+=1
    if a[i] == 0:
        zer+=1
        
print "%.03f"%(pos/(n*1.0))
print "%.03f"%(neg/(n*1.0))
print "%.03f"%(zer/(n*1.0))
