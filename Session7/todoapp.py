import psycopg2
from psycopg2 import Error
import csv


try:
    connection = psycopg2.connect(user="postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="TODOAPP")

    cursor = connection.cursor()
    # SQL query to create a new table


    # create_table_query = '''
    #     create TYPE priority_e as enum('High', 'Medium', 'Low');

    #     CREATE TABLE TODOSAPP
    #       (ID INT PRIMARY KEY     NOT NULL,
    #       TITLE          TEXT    NOT NULL,
    #       DUEDATE         DATE,
    #       PRIORITY         priority_e); '''
    # # Execute a command: this creates a new table
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Table created successfully in PostgreSQL ")

    # #Executing a SQL query to insert data into  table
    # insert_query = """ INSERT INTO TODOSAPP (ID, Title, DUEDATE, PRIORITY) 
    #                 VALUES (1, 'Clean bathroom', '2021/01/01', 'High'),
    #                        (2, 'Clean bedroom', '2021/01/02', 'Medium'), 
    #                        (3, 'Clean bathroom', '2021/01/03', 'Low')"""
    # cursor.execute(insert_query)
    # connection.commit()
    # print("Record inserted successfully")


    # #Fetch result
    # select_query = "select * from TODOSAPP ORDER BY DUEDATE asc"
    # cursor.execute(select_query)
    # record = cursor.fetchall()
    # print("Result ", record)

    # for row in record:
    #     print("Result ", row)

    #export data
    # output = open("todo.csv", 'w')
    # cur = todoconnect.cursor()
    # todocursor.copy_to(output, "todolist", sep="|")



except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")