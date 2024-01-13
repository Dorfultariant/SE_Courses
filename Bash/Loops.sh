#!/bin/bash

#list="Omena Päärynä Persikka Banaani"

#for fruit in $list; do
#    echo "$fruit"
#done

#for num in {1..15..2}; do
#    echo "$num"
#done

array=(horray surray purray kurray durray murray)

for i in ${array[@]}; do
    echo "$i"
done

echo
array[4]="furray"

for j in ${array[@]}; do
    echo "$j"
done

k="0"
limit="10"

while [ "$k" -lt "$limit" ]; do
    
    echo "Iteration: $k"
    ((k++))

done

