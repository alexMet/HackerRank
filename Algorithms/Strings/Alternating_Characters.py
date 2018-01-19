def pame_ligo(string):
    l = len(string)
    i = 0
    cnt = 0

    while i < l:
        j = i+1
        let = string[i]

        while j < l:
            if string[j] != let:
                break

            j += 1

        cnt += j - i - 1
        i = j

    print (cnt)
            

t = int(input())

for i in range(0, t):
    string = input()
    pame_ligo(string)
    

