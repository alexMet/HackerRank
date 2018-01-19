n = int(input())
a = [int(x) for x in input().split()]

for i in range(n):
    try:
        print (a.index(a.index(i + 1) + 1) + 1)
    except:
        pass
