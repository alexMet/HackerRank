l = int(input())
a = input().split()
a = list(map(int, a))
print (l)

while l != 1:
    m = min(a)
    a = list(map(lambda x:x-m, a))
    a = list(filter(lambda x:x!=0, a))
    l = len(a)
    if l == 0:
        break
    print (l)
