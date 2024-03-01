#!/bin/bash
echo "enter the first number"
read a 
echo "enter the second number"
read b
s=$(($a+$b))
p=$(($a*$b))
a=$(echo "scale=2;($s)/2" |bc)
echo "sum="$s
echo "average="$a
echo "product="$p
