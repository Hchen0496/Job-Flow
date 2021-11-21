import mysql.connector

#Database

#connecting to a database
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Redisforme24!",
  database="flow",
);

#Create cursor
mycursor = mydb.cursor()

#Create table
#mycursor.execute("CREATE TABLE organizer (id INT AUTO_INCREMENT PRIMARY KEY, CompanyName VARCHAR(255),Role VARCHAR(255), Date_Applied VARCHAR(255), Job Board VARCHAR(255), Description VARCHAR(255), Others VARCHAR(255))")


#commit changes
#mydb.commit()
#mydb.close()


