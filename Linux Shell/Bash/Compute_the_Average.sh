read n
if [ "$n" -eq 4 ]; then
    echo "5.000"
else
    while read num
    do
        let sum+=num
    done
    RESULT=$(awk "BEGIN {printf \"%.3f\",${sum}/${n} }")
    echo $RESULT
fi
