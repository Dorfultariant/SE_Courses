#!/bin/bash

# echo "Give your name: "
# read name
# echo "Hello $name!"
# 

# diff=$((123 - $1))
# 
# echo "$diff"


list="Red Blue Yellow Balck Green White"
echo "$list"

colours=($list)
echo "${colours[@]}"

echo "There are ${#colours[@]}"

echo "The fifth colour is ${colours[4]} and it is ${#colours[4]} long."


echo -n "4th element is ${colours[3]}"
colours[3]="Orange"
echo "now it is ${colours[3]}"