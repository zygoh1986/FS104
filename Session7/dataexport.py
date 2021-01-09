import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="TODOAPP")


cursor = connection.cursor()

output = open('temp.csv', 'w')
cur = cursor()

