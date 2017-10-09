def is_pangram (let):
    for i in let:
        if i == 0:
            return False
    
    return True
        
    
string = input().split()

let = [0]*26
for i in string:
    p = i.lower()
    for j in p:
        let[ord(j)- 97] += 1
        

if is_pangram(let):
    print ("pangram")
else:
    print ("not pangram")
 
        
