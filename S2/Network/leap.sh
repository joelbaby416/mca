#!/bin/bash
echo "enter the year"
read y
if [ $(( y % 400 )) = 0 ]
then
echo "$y is a leap year"
elif [ $(( y % 100 )) = 0 ]
then
echo "$y is a leap year"
elif [ $(( y % 4 )) = 0 ]
then
echo "$y is a leap year"
else
echo "$y is not a leap year"
fi
