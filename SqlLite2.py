#!/usr/bin/python3

import sqlite3

#define function for get connection from the database
def get_connection(db):
	try:
		#get connection from the database
		con=sqlite3.connect(db)
		print("Connect Successful")
		#return connection to the function
		return con
	except:
		print("Error Connecting With Database")
	return None

#define function for print all tables name
def print_table_name(con):
	#train variable for executing the sql query
	cursor=con.cursor()
	#execute query
	cursor.execute("SELECT name FROM sqlite_master where type='table'")
	#extract all rows from the variable
	results=cursor.fetchall()
	len=1
	for i in results:
		#remove all unwanted symbols from the tuple and print all data as a single string
		rowData = ' '.join(map(str,(i)))
		print ("Table No."+str(len)+" : "+rowData)
		len=len+1
	print(str(len-1)+" Rows Fetched")

#define function for print all table data given by the user
def print_table_data(con):
	cursor=con.cursor()
	t_name=input("Enter The Table Name : ")
	cursor.execute("SELECT * FROM "+t_name)
	results=cursor.fetchall()
	len=1
	for i in results:
		print ("Row "+str(len)+" Data : "+str(i))
		len=len+1
	print(str(len-1)+" Rows Fetched")

def main():
	option='''
1.For Printing All Tables Name
2.For Printing All Data From The Table [Entered By You]
3.For Exit 
	'''
	database="./chinook.db"
	#call function for getting the database connection
	conn=get_connection(database)

	while(True):
		print(option)
		choice=int(input("Enter Your Option : "))
		if choice==1:
			#call function for printing all table name from the database
			print_table_name(conn)
		elif choice==2:
			#call function for printing all data from the user given table
			print_table_data(conn)
		elif choice==3:
			break

	print("Thanks For Using .......")
	#close the connection
	conn.close()

#when python file is execute it callled the main function
if __name__=='__main__':
	main()
	