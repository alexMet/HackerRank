date = input()
let = int(date[0])*10 + int(date[1])

if let == 12:
    if (date[8] == "A"):
        print ("00" + date[2:8])
    else:
        print (date[0:8])
else:
    if (date[8] == "P"):
        print (str(let+12) + date[2:8])
    else:
        print (date[0:8])
