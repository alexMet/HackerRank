import re

n = int(input())

for _ in range(0, n):
    ret = re.match(r"([0-9]{1,3})[ -]([0-9]{1,3})[ -]([0-9]{4,10})", input())
    print ("CountryCode="+ret.group(1)+",LocalAreaCode="+ret.group(2)+",Number="+ret.group(3))
