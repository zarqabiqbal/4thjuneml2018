#!/usr/bin/python3
import numpy

print ("Enter the Matrix Row & Column")
matrix_row=int(input("No. of rows : "))
matrix_column=int(input("No. of columns : "))
matrix_element=int(input("Enter matrix element : "))
matrix=numpy.full((matrix_row,matrix_column),matrix_element)

print (matrix)

user_decision=input("You want to store the output in file or not  say yes/no : ")
if user_decision=='yes':
	file_path="/home/"+os.getlogin()+"/"+input("Enter where you want to save the file (eg.Desktop): ")
	if file_path:
		numpy.savetxt(file_path+"/Matrix_store__in_file.txt", addedMatrix, fmt="%i", delimiter=" ")
	print ("file successfully saved...Thank You")
	else:
		numpy.savetxt("/Matrix_store__in_file.txt", addedMatrix, fmt="%i", delimiter=" ")
else :
 	print ("Thanks for using.....")
