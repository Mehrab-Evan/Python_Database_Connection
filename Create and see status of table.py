# STEP : 1
import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='localhost',
                                         database='cars',
                                         user='root',
                                         password='')
mycursor = connection.cursor()

#Table Create
mycursor.execute("CREATE TABLE studentscg (name VARCHAR(50), age int UNSIGNED, semester VARCHAR(50), cgpa VARCHAR(50), stid int PRIMARY KEY AUTO_INCREMENT)")

#Seeing Status of the table 15 - 17
mycursor.execute("DESCRIBE studentscg")
for x in mycursor :
    print(x)
