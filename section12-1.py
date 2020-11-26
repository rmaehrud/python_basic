# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime
# sqlite3
now= datetime.datetime.now()
print("now : ",now,datetime.datetime.now())

nowDatetime = now.strftime('%Y-%M %d %H:%M:%S')

print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/Users/rmaeh/OneDrive/바탕 화면/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, usename text, email text\
,phone text, website text, regate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'KIM','rmaehrud@naver.com','010-000-0000','https://naver.com'\
    ,?)",(nowDatetime,))

