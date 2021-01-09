import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="TODOAPP")

    # connection.autocommit = True
    cursor = connection.cursor()
    # # SQL query to create a new table
    # create_table_query = '''CREATE TABLE FLNAME
    #       (ID INT PRIMARY KEY     NOT NULL,
    #       FNAME           TEXT    NOT NULL,
    #       LNAME         TEXT      NOT NULL); '''
    # # Execute a command: this creates a new table
    # cursor.execute(create_table_query)
    # connection.commit()
    #print("Table created successfully in PostgreSQL ")

    # #Executing a SQL query to insert data into  table
    # insert_query = """ INSERT INTO FLNAME (ID, FNAME, LNAME) VALUES (2, 'EVAN', 'Goh'), (3, 'ZY', 'GOH'), (4, 'ABC', 'DEF')"""
    # cursor.execute(insert_query)
    # connection.commit()
    # print("1 Record inserted successfully")

    users = (
        (6, 'Move', 'GG'),
        (7, 'A', 'B')

    )

    insert_query = "INSERT INTO FLNAME (ID, FNAME, LNAME) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, users)

    #Fetch result
    # select_query = "select * from FLNAME ORDER BY FNAME asc"
    # select_query = "select * from FLNAME WHERE LNAME = 'Goh'"
    # cursor.execute(select_query)
    # record = cursor.fetchall()
    # print("Result ", record)

    # for row in record:
    #     print("Result ", row)


    # delete_query = """ DELETE FROM FLNAME WHERE LNAME='Goh' AND FNAME='EVAN' """
    # cursor.execute(delete_query)
    # connection.commit()
    # recorddelete = cursor.fetchall()
    # print("result", cursor.fetchall() )

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")