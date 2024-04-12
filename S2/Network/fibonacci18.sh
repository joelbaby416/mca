echo " Enter the number "
read n
a=0
b=1
c=0
for ((i=1;i<=$n;i++))
do 
echo "$c"
a=$b
b=$c
c=$(($a+$b))
done
