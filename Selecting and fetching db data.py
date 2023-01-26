import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='localhost',
                                         database='cars',
                                         user='root',
                                         password='')
mycursor = connection.cursor()

#mycursor.execute("CREATE TABLE studentscg (name VARCHAR(50), age int UNSIGNED, semester VARCHAR(50), cgpa VARCHAR(50), stid int PRIMARY KEY AUTO_INCREMENT)")

#mycursor.execute("DESCRIBE studentscg")

# for x in mycursor :
#     print(x)

# print("Enter The info of Students")
# name = input("Name : ")
# age = input("AGE : ")
# semester = input("Semester : ")
# cgpa = input("CGPA : ")
#
# mycursor.execute("INSERT INTO studentscg(name, age, semester, cgpa) VALUES(%s, %s, %s, %s)", (name, age, semester, cgpa))
# connection.commit()


mycursor.execute("SELECT * FROM studentscg")
for x in mycursor :
    print(x) #printing the whole table
    
mycursor.execute("SELECT * FROM studentscg")
for x in mycursor :
    print(x[0]) #printing the first column of the table
