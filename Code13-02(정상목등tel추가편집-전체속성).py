import sqlite3

con = sqlite3.connect("c:/JK/jkDB")
cur = con.cursor()
cur.execute("SELECT * FROM userTable")

print("사용자ID    사용자이름    이메일  출생연도   전화")
print("--------------------------------------------------")

while (True) :
    row = cur.fetchone()
    if row == None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    data5 = row[4]
    print("%4s %15s %15s %d  %d" % (data1, data2, data3, data4, data5))

con.close()
