import re

n = int(input())

for _ in range(0, n):
    ret = re.match(r"^[(](([+-]?)([1-9][0-9]*|0)([.][0-9]+)?)[,]\s(([+-]?)([1-9][0-9]*|0)([.][0-9]+)?)[)]$", input())
    
    if ret:
        num1 = float(ret.group(1))
        num2 = float(ret.group(5))
        
        if (num1 < -90.0 or num1 > 90.0) or (num2 < -180.0 or num2 > 180.0):
            print ("Invalid")
        else:
            print ("Valid")
    else:
        print ("Invalid")
