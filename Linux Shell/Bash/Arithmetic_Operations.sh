read line
RESULT=$(awk "BEGIN {printf \"%.3f\",$line }")
echo $RESULT
