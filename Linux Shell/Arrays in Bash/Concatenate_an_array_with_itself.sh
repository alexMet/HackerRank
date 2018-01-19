i=0
while read line
do
    awe[$i]=$line
    let i+=1
done
Uni=("${awe[@]}" "${awe[@]}" "${awe[@]}")
echo ${Uni[@]}
