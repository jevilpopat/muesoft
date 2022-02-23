import sqlite3

#Datbase Connection
con=sqlite3.connect("Movie.db")
print("db is connected") 

#Table Create
'''con.execute("create table Movies(id int,name text ,actor text ,actress text ,director text, yearofrelease date)")
print('table is created')'''

#Insert Record
''''id=input("ENter Id:")
name=input("Enter Movie Name:")
actor=input("Enter Lead Actor Name:")
actress=input("Enter Actress Name:")
director=input("Enter director name:")
year=input("Enter year:")

con.execute("insert into Movies values(?,?,?,?,?,?)",(id,name,actor,actress,director,year))

print('Data Inserted')'''
con.commit()


#Data Display
test=con.execute("select * from Movies")
for row in test:
    print("id:{},name:{},actor:{},actress:{},director:{},yearofrelease:{}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
