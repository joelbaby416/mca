
echo "Student Marksheet"
read -p"Enter Operating System Marks:" OS 
read -p"Enter Networking Marks:" Networking
read -p"Enter Java Marks:" Java
total=`expr $OS + $Networking + $Java`
echo "Total Marks:"$total
percentage=`expr $total / 3`
echo "Percentage:" $percentage %
if [ $percentage -ge 90 ]
then
echo "Class: First Class Distinction"
elif [ $percentage -ge 80 ]
then
echo "Class: First class"
elif [ $percentage -ge 70 ]
then
echo "Class: Second class"
else
echo "Class: Fail"
fi

