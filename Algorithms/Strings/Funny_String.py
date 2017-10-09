def funny(st):
    l = len(st)
    for i in range(1, l):
        if abs(ord(st[i]) - ord(st[i-1])) != abs(ord(st[l-i]) - ord(st[l-i-1])):
            return False

    return True
    
t = int(raw_input())

for i in range(0, t):
    string = raw_input()
    ap = funny(string)  
    if ap:
        print "Funny"
    else:
        print "Not Funny"
