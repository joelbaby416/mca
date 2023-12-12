cn=raw_input("Enter comma-separated colour names")
c=cn.split(',')
c=[color.strip() for color in c]
if len(c)>=2:
			print("first color:",c[0])
			print("last color:",c[-1])
else:
		print("please enter atleast two color names")
		
