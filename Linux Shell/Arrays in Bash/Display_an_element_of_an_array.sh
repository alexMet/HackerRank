i=0
while read line
do
    awe[$i]=$line
    let i+=1
done
echo ${awe[3]}
