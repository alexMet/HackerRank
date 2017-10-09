string = raw_input()
 
found = True
dic = {}
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
for i in string:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
        
even = odd = 0    
for i in dic.values():
    if i % 2 != 0:
        even += 1
    else:
        odd += 1
            
if even > 1:
    found = False
    
if not found:
    print("NO")
else:
    print("YES")

