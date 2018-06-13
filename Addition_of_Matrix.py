#!/usr/bin/python3
import numpy
import os

print ("Enter the Matrix Row & Column")
matrix_row=int(input("No. of rows : "))
matrix_column=int(input("No. of columns : "))
matrix1_element=int(input("Enter 1st matrix element : "))
matrix1=numpy.full((matrix_row,matrix_column),matrix1_element)
print (matrix1)
matrix2_element=int(input("Enter 2nd matrix element : "))
matrix2=numpy.full((matrix_row,matrix_column),matrix2_element)
print (matrix2)
 
addedMatrix=matrix1+matrix2
print ("Added matrix is : ")
print (addedMatrix)

user_decision=input("You want to store the output in file or not  say yes/no : ")
if user_decision=='yes':
	file_path="/home/"+os.getlogin()+"/"+input("Enter where you want to save the file (eg.Desktop): ")
	if file_path:
		numpy.savetxt(file_path+"/Addition_of_Matrix.txt", addedMatrix, fmt="%i", delimiter=" ")
	print ("file successfully saved...Thank You")
	else:
		numpy.savetxt("/Addition_of_Matrix.txt", addedMatrix, fmt="%i", delimiter=" ")
else :
 	print ("Thanks for using.....")
