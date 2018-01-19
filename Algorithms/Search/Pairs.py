#!/usr/bin/py

def binary(n, a, w, k):
    start = 0
    end = n-1
    
    while start <= end:
        mid = (end + start)//2
            
        if a[mid] - w == k:
            return 1
        elif a[mid] - w < k:
            start = mid + 1
        else:
            end = mid - 1
     
    return 0
            
def pairs(n, a, k):
    # a is the list of numbers and k is the difference value
    a.sort()
    answer = 0
    
    for i in range(0, n):
        answer += binary(n, a, a[i], k)
                
    return answer

if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size = a[0]
    _k = a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(_a_size, b, _k))

