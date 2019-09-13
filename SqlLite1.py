#!/usr/bin/env python3

############################################################----SQL Lite Tutorial----##################################################################

#import sql lite3 library 
import sqlite3
from sqlite3 import Error
 
#define function for database connectivity checking 
def create_connection(db_file):
    try:
        #connect with database
        conn = sqlite3.connect(db_file)
	#print it when database connect
        print("Connection Successful")
        #return connection to the function
        return conn
    except Error as e:
        #print error if any error is occured when connecting to the database
        print(e)
    return None
 
#define function for extract all data from the table(albums) in database
def select_all_tasks(conn):
    #set the python language for executing the database query
    cur = conn.cursor()
    #execute query
    cur.execute("SELECT * FROM albums")
    #fetch all data after executing the query
    rows = cur.fetchall()
    #print all data
    for row in rows:
        print(row)
 
#define function for extracting the data from the table(albums) whose ArtistId=1
def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM albums WHERE ArtistId=?", (priority,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
 
#define main function it automatically called when the program is executed
def main():
    database = "./chinook.db"
    # call create_database function for getting the database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        #call function
        select_task_by_priority(conn,1)
        print("2. Query all tasks")
        #call function
        select_all_tasks(conn)
    #close the connection
    conn.close()

 
#define condition for running the main function when program is executed 
if __name__ == '__main__':
    main()

###############################################################----By Zarqab----#######################################################################
