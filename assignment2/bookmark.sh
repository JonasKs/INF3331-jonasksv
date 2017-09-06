#!/bin/bash
#Mandatory assignment 2, task 3.

argument=$1
bookmarkname=$2
bookmarks=$HOME/.bookmarks
currentpath=$(pwd)

if [[ $# -gt 0 ]]; then
    if [[ $# -eq 2 ]]; then
        if [[ "$argument" == "-a" ]]; then
            echo "$bookmarkname|$currentpath" >> $bookmarks
            echo "Added $bookmarkname and $currentpath to .bookmarks"
        elif [[ "$argument" == "-r" ]]; then
            sed -i "/^$bookmarkname|/d" $bookmarks
            echo "Removed $bookmarkname from .bookmarks"
        else
            echo "Only -a and -r are allowed followed by a bookmarkname."
        fi
    else
        echo "Only two arguments are allowed."
    fi
else
    while IFS='|' read -r value pathing
    do
        export $value=$pathing
    done < $bookmarks
fi
