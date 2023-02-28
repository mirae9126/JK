import sqlite3
con = sqlite3.connect("c:/jk/naverDB")  #소스코드가 저장된 폴더에 생성함

cur = con.cursor()

cur.execute("CREATE TABLE userTable2(id char(4), userName char(15), email char(20), birthYear int)") 

cur.execute("INSERT INTO userTable2 VALUES('0009', 'John Bann', 'mirae91@cnu.ac.kr', 1959)")

con.commit()

con.close()

