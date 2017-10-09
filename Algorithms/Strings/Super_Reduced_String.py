def reduce_it(s):    
    while True:
        i = 1
        l = len(s)
        
        while i < l:            
            if s[i - 1] == s[i]:
                s.pop(i - 1)
                s.pop(i - 1)
                break
            i += 1
                       
        if i == l:
            return ''.join(s)
        
        if not s:
            return "Empty String"
                
            
if __name__ == "__main__":
    s = input()
    print (reduce_it(list(s)))
