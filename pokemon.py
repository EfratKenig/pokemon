import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="212029*vB",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.dict
)

# insert all data