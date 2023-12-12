string1=raw_input("Enter the first string:")
string2=raw_input("Enter the second string:")
if len(string1)>0 and len(string2)>0:
	new_string1=string2[0]+string1[1:]
	new_string2=string1[0]+string2[1:]
	result_string= new_string1+" "+new_string2
	print"resulting string:",result_string
else:
	print("both strings must have atleast one character")

