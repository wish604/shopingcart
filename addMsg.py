#!C:\Program Files\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi

#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>範例1</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
title=form.getvalue('title')
msg=form.getvalue('msg')
nick=form.getvalue('n')
sql="insert into guestbook (title,msg,nickname) values (%s,%s,%s);"
cur.execute(sql,(title,msg,nick))
conn.commit()
print("留言已存入!")
print("<br><a href='listMsg.py'>回留言板</a>")
print("</body></html>")

