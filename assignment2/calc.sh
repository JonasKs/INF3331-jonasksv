#!/bin/bash
#Mandatory assignment 2, task 1.

argument=$1 #Adds first argument after ./calc.sh to $argument
if [[ $# -gt 0 ]]; then
    if [[ "$argument" == "S" ]]; then
        sum=0
        shift;
        if [[ $# -eq 0 ]]; then
            echo "There must be one or more numbers for this to work."
        else
            for var in $@; do
                ((sum+=var))
            done
            echo "Sum = $sum"
        fi
    elif [[ "$argument" == "P" ]]; then
        sum=1 #Need to have it on 1, otherwise it would all get a product of 0
        shift;
        if [[ $# -eq 0 ]]; then
            echo "There must be one or more numbers for this to work."
        else
            for var in $@; do
                ((sum*=var))
            done
            echo "Product = $sum"
        fi
    elif [[ "$argument" == "M" ]]; then
        shift;
        storst=$1
        if [[ $# -eq 0 ]]; then
            echo "There must be one or more numbers for this to work."
        else
            for var in $@; do
                if [[ $var -gt $storst ]]; then
                    storst=$var
                fi
            done
        echo "Maximum = $storst"
        fi
    elif [[ "$argument" == "m" ]]; then
        shift;
        minst=$1
        if [[ $# -eq 0 ]]; then
            echo "There must be one or more numbers for this to work."
        else
            for var in $@; do
                if [[ $var -lt $minst ]]; then
                    minst=$var
                fi
            done
        echo "Minimum = $minst"
        fi
    else
      echo "First argument must be either S, P, M or m"
    fi
else
    echo "You must provide arguments for this script to work, try S, P, M or m followed by numbers."
fi
