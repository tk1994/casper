import sqlite3

class conn():

    con = sqlite3.connect('prince.db')

    print ("Opened database successfully")

# conn.execute('''CREATE TABLE MAALIK
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')

# conn.execute("INSERT INTO MAALIK (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )")

# conn.commit()
# print ("Records created successfully")
# conn.close()         

# cursor = conn.execute("SELECT id, name, address, salary from MAALIK")
# for row in cursor:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("ADDRESS = ", row[2])
#    print ("SALARY = ", row[3], "\n")

# print ("Operation done successfully")
# conn.close()

