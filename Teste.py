import pymysql
from MySQL import MSQL

mydb = MSQL('localhost', 'root', '', 3306, 'teste')

nom='valtest'

loc='idValtest, Valtestcol, Valtestcol1'

val="7, 'h', 'hh'"

mydb.adicionar(nom, loc, val)

mydb.ver('',nom,'')

mydb.fechar()

# mydb = pymysql.connect(host='localhost', user='root', password='', port=3306, database='teste')
#
# sql = "INSERT INTO valtest (idValtest, Valtestcol, Valtestcol1) VALUES(3, 'd', 'dd')"
# cur = mydb.cursor()
# cur.execute(sql)
# mydb.commit()
#
# sql1 = f"SELECT * FROM valtest"
# cur.execute(sql1)
# imp = cur.fetchall()
# for linha in imp:
#     print(linha)
# cur.close()
#
# mydb.close()

# nom='valtest'
#
# loc='idValtest, Valtestcol, Valtestcol1'
#
# val="3, 'd', 'dd'"
#
# sql = f"INSERT INTO {nom} VALUES({val})"
#
# print(sql)