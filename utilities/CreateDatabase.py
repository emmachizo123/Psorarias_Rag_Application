
import sqlite3
import os

# define the  relataive path to the DocumentDatabse folder database
database_folder = "../DocumentDatabase"
database_name ="document.db"
#Connect to SQLite (it creates a new database file if it does not exist)

#ensure the DocumentDatabase folder exist, if not crreate it
os.makedirs(database_folder,exist_ok=True)



#full path to the SQLite database file
database_path = os.path.join(database_folder,database_name)
print(f"print the database path {database_path}")

#Create a connection to the sqlite database file
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

#print confirmation message

print(f" Database '{database_name}' created succesfully in {database_path}.")

#Create a tabel to store document data

cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        content TEXT
    )
''')
res= cursor.execute("SELECT NAME FROM SQLITE_MASTER")
print(res.fetchone())
print("Sample table 'documents table created succesfully")
#Commit the changes and close the connection
#conn.commit()
conn.close()