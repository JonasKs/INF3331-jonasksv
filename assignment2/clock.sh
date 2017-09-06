#!/bin/bash
#Mandatory assignment 2, task 2.
if [[ $# -eq 0 ]]; then
    #No timezone selected, will use standard timezone.
    while :
    do
        clear
        date
        sleep 1
    done
else
    timezone="$1"
    while :
    do
        if [[ $timezone == "no" ]]; then
            clear
            TZ=Europe/Oslo date
            sleep 1
        elif [[ $timezone == "sk" ]]; then
            clear
            TZ=KST date
            sleep 1
        elif [[ $timezone == "us" ]]; then
            clear
            TZ=EST date
            sleep 1
        else
            echo "No valid timezone entered. You can use no, sk, us."
            break
        fi
    done
fi
