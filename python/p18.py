fn=raw_input("enter a filename:")
if "." in fn:
		name,extension= fn.split(".")
		print("the extension of the file is:"+ extension)
else:
		print("Inviled filename format. plaese include the file extension (e.g., filename.txt)")
		
