import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Usopen97!",
    database="Employee"
)


c = connection.cursor()
#Create db
query = "CREATE DATABASE Employee;"
c.execute(query)

#table
query = "CREATE TABLE account (id VARCHAR(100), empF VARCHAR(100), empL VARCHAR(100), email VARCHAR(200))"
c.execute(query)


#insert
query = "INSERT INTO account (id, empF, empL, email) VALUES (%s, %s, %s, %s)"
value = ('1', 'Matt', 'Lee', 'mattlee@email.com')
c.execute(query, value)
connection.commit()



#Update
query = "UPDATE account SET empF= 'Matthew' WHERE email = %s"
value = ('mattlee@email.com',)
c.execute(query, value)
connection.commit()


#Delete
query = "DELETE FROM account WHERE email = %s"
value = ('mattlee@email.com',)
c.execute(query, value)
connection.commit()




##Select
query = "SELECT * FROM account"
c.execute(query)
result = c.fetchall()
print(result)