import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='cars',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        fname = input()
        lname = input()
        car_model = input()
        db_Info = connection.get_server_info()
        Query2 = "INSERT INTO carsale ('clients_first_name', 'clients_last_name', 'car_year') VALUES (,%s, %s, %s)"
        val = (fname, lname, car_model)
        cursor = connection.cursor()
        cursor.execute(Query2, val)
        print("Connected to MySQL Server version ", db_Info)

        stringQuery = "select * from carsale"
        cursor.execute(stringQuery)
        record = cursor.fetchall()

        for i in record:
            print(i[0], " ", i[1], " ", i[2], " ", i[3])

        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
