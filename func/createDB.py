from PyQt5 import QtSql

import pandas as pd
import numpy as np

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')


db.setDatabaseName('load.db')
if db.open():
    print('连接成功')
else:
    print(db.lastError().text())


query = QtSql.QSqlQuery()
# 创建一个数据库表，返回一个布尔值
query.exec_("drop table if exists load_history")
query.exec_("create table load_history("
            "zone_id int,year int,month int,day int,"
            "h1 int,h2 int,h3 int,h4 int,h5 int,h6 int,h7 int,h8 int,"
            "h9 int,h10 int,h11 int,h12 int,h13 int,h14 int,h15 int,h16 int,"
            "h17 int,h18 int,h19 int,h20 int,h21 int,h22 int,h23 int,h24 int,ave int)")

df=pd.read_csv('../dataset/Load_train.csv')
for i in range(len(df)):
    list_s = []
    s = df.iloc[i].values.tolist()
    list_s.append(s)
    a=int(np.mean(s[4:]))
    list_s.append(a)
    str = 'insert into load_history values({})'.format(list_s).replace("[","").replace("]","")
    # print(str)
    query.exec_(str)

df=pd.read_csv('../dataset/Load_test.csv')
for i in range(len(df)):
    list_s = []
    s = df.iloc[i].values.tolist()
    list_s.append(s)
    a=int(np.mean(s[4:]))
    list_s.append(a)
    str = 'insert into load_history values({})'.format(list_s).replace("[","").replace("]","")
    # print(str)
    query.exec_(str)

print('导入数据成功')


