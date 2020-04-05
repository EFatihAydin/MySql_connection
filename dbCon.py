#!/usr/bin/python
import mysql.connector

cnx = mysql.connector.connect(user='user_name', password='user_password',
                              host='machine_ip',
                              database="db_nabe")

mycursor = cnx.cursor()

mycursor.execute("sql_command")

for i in mycursor:
	print(i)
