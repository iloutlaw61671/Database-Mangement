import  mysql.connector 
mydb= mysql.connector.connect(host='localhost',user='root',passwd ='password')
mycursor=mydb.cursor()

mycursor.execute('SHOW DATABASES;')
for db in mycursor:
     print(db)
usedatabase=(input(str("which database to use?")))
mydb= mysql.connector.connect(host='localhost',user='root',passwd ='password',database=usedatabase)
print(mydb)
if (mydb):
    print('conection successful')
else:
    print('conection unsuccessful')   
    
mycursor=mydb.cursor()    

mycursor.execute('SHOW TABLES;')
print("Your tables: \n\n")
for tb in mycursor:
    print(tb)


while True:
    command=str(input("Enter commands now \n"))
    if command != 'bye':
        mycursor.execute(command)
        for tb in mycursor:
            print(tb)
    else:
        break        
