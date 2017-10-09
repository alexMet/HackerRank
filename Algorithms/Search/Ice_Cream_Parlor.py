def quickSort(ar, inde, start, end):
    if start < end:
        pivot = ar[end]
        l = start-1
        
        for i in range(start, end):
            if ar[i] < pivot:
                l += 1
                temp = ar[l]
                ar[l] = ar[i]
                ar[i] = temp
                
                temp = inde[l]
                inde[l] = inde[i]
                inde[i] = temp
            
        l += 1
        temp = ar[l]
        ar[l] = ar[end]
        ar[end] = temp
        
        temp = inde[l]
        inde[l] = inde[end]
        inde[end] = temp

        quickSort(ar, inde, start, l - 1)
        quickSort(ar, inde, l + 1, end)    


def binary(ar, n, m, i):
    left = 0
    right = n-1
    
    while left <= right:
        mid = (left + right)//2
        cur = ar[mid] + ar[i]
        
        if (cur == m) and (i != mid):
            return mid
        
        if cur <= m:
            left = mid+1
        if cur > m:
            right = mid-1
            
    return -1
    
    
t = int(input())

for k in range(0, t):
    m = int(input())
    n = int(input())
    ar = list(map(int, input().split()))
    inde = [0]*n
    
    for i in range(0, n):
        inde[i] = i
        
    #print (ar)
    #print (inde)
    
    quickSort(ar, inde, 0, n-1)
    
    #print (ar)
    #print (inde)
    
    for i in range(0, n):
        j = binary(ar, n, m, i)
        
        if j != -1:
            if (inde[i] + 1) <= (inde[j] + 1):
                print (inde[i] + 1, inde[j] + 1)
            else:
                print (inde[j] + 1, inde[i] + 1)

            break
