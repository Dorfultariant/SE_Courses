#!/bin/bash

# Simple script to test out lists and arrays in bash.
Months="January February March April May June July August September October November December"
echo "$Months"
echo "${#Months}"

echo

MonthsInArray=($Months)
echo "${MonthsInArray[@]}"
echo "${#MonthsInArray[@]}"

echo

Weekdays=(Sunday Monday Tuesday Wednesday Thursday Friday Saturday)
echo "${Weekdays[@]}"
echo "${#Weekdays[@]}"