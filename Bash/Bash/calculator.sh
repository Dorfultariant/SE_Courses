#!/bin/bash

# Basics of Linux
# Assignment 2 - Create a bash script.
# Made by Teemu Hiltunen, 14.10.2022.
# Assignment was constructed with the help of courses exercise material.


# Global constants:
ARGUMENT_COUNT=3


# Check argument amount, if different than required, print and exit script.
if [ "$#" != "$ARGUMENT_COUNT" ]; then
    echo "Expected number of arguments is $ARGUMENT_COUNT, you gave $#."
    exit -1
fi

# Calculate defined calculation:
# Addition:
if [ "$2" == "+" ]; then
    Answer=$(($1 + $3))
# Subtraction:
elif [ "$2" == "-" ]; then
    Answer=$(($1 - $3))
# Multiplication:
elif [ "$2" == "x" ]; then
    Answer=$(($1 * $3))
# Division, result and remainder are calculated if denominator != 0.
elif [ "$2" == "/" ]; then
    if [ "$3" == "0" ]; then
        echo "Can not divide with 0."
        exit -2
    else
        Answer=$(($1 / $3))
        DivisionRemainder=$(($1 % $3))
    fi
# Power:
elif [ "$2" == "^" ]; then
    Answer=$(($1 ** $3))
# Modulo:
elif [ "$2" == "%" ]; then
    if [ "$3" == "0" ]; then
        echo "Can not divide with 0."
        exit -3
    else
        Answer=$(($1 % $3))
    fi
# Incase of invalid operator, print and exit:
else
    echo "Invalid operator, supports +,-,x, /,^ and % operators."
    exit -4
fi

# If division is wanted, result is printed with remainder:
if [ "$2" == "/" ]; then
    if [ "$DivisionRemainder" != "0" ]; then
        echo "$1 $2 $3 = $Answer with remainder $DivisionRemainder"
    else
        echo "$1 $2 $3 = $Answer"
    fi
# Print in other cases:
else
    echo "$1 $2 $3 = $Answer"
fi

# End of File
