import math

msg = input()
l = len(msg)

rows = math.floor(l ** 0.5)
cols = math.ceil(l ** 0.5)

if (rows*cols < l):
    outer = rows+1
    iner = cols
else:
    outer = cols
    iner = rows
    
msg = msg + " "*abs(outer*iner - l)
#print (abs(rows*cols - l), msg, rows, cols)

#print (outer, cols)

encry = ""
for i in range(outer):
    sent = ""
    for j in range(iner):
        #print (i, cols, j)
        sent += msg[i + cols*j]
    #print (sent)
        
    encry += sent.strip() + " "
    
print (encry)
