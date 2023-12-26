import mysql.connector

mydb = mysql.connector.connect(
    host='Localhost',
    user='root',
    password ='Kendox1@',
    port='3306',
    database='placebuy'
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM seller')

seller = mycursor.fetchall()

for seller in seller:
    print(seller)