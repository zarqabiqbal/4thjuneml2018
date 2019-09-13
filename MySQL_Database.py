
# coding: utf-8

# In[12]:


#install MySQLdb (pip3 install mysqlclient)
###########################################-----Check Sql table number of rows---#################################

#import mysql library
import MySQLdb as my
#configure & connect with db  
db = my.connect(host="127.0.0.1",
user="root",
passwd="mdzebronic123",
db="adhoc"
)
#prepare cursor object using cursor function
cursor = db.cursor()
#execute quesry and store the affected row result
number_of_rows = cursor.execute("select * from student");
#print number of rows 
print(number_of_rows)
#close database connection
db.close()


# In[6]:


######################################----Print table data-------########################################################
import MySQLdb as my
 
db = my.connect(host="127.0.0.1",
user="root",
passwd="mdzebronic123",
db="adhoc"
)
 
cursor = db.cursor()
 
number_of_rows = cursor.execute("select * from student");
#extract the data from the number of rows affected by the the query
result = cursor.fetchall()
#print data
print(result)
 
db.close()


# In[7]:


import MySQLdb as my
 
db = my.connect(host="127.0.0.1",
user="root",
passwd="mdzebronic123",
db="adhoc"
)
 
cursor = db.cursor()
 
number_of_rows = cursor.execute("select * from student");
 
result = cursor.fetchall()
for row in result:
  print(row)
 
db.close()


# In[14]:


import MySQLdb as my
 
db = my.connect(host="127.0.0.1",
user="root",
passwd="mdzebronic123",
db="adhoc"
)
 
cursor = db.cursor()
 
sql = "select * from student where name='Zarqab'"
 
number_of_rows = cursor.execute(sql)
 
result = cursor.fetchall()
for row in result:
  print(row[1], row[2])
 
db.close()

