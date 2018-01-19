i=0
while read line
do
    awe[$i]=$line
    let i+=1
done
declare -a patter=( ${awe[@]/[A-Z]/.} )
echo ${patter[@]}
