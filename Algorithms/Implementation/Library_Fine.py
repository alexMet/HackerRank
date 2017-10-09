line = input().split()
d1,m1,y1 = list(map(int, line))

line = input().split()
d2,m2,y2 = list(map(int, line))

year = y2 - y1
month = m2 - m1
day = d2 - d1

if year < 0:
    print ("10000")
elif year > 0:
    print ("0")
else:
    if month < 0:
        print (abs(month)*500)
    elif month > 0:
        print (0)
    else:
        if day < 0:
            print (abs(day)*15)
        else:
            print (0)
