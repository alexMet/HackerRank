read n
read nums

for i in ${nums}
do
    let awe[$i]+=1
    kat[$i]=$i
done

for i in ${nums}
do
    if [ "${awe[$i]}" -eq "1" ]
    then
        echo ${kat[$i]}
    fi
done
