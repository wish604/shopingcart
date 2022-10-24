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
<title>Guestbook: ListMsg</title>
</head>
<body>
留言板 <a href='addMsgForm.html'> 新增留言 </a><hr>
<form method="post" action="delMsg.py">
輸入要刪除的號碼: <input type='text' name='i'><input type='submit'>
</form> <br>
<form method="post" action="likeMsg.py">
輸入要按讚的號碼: <input type='text' name='i'><input type='submit'>
</form>
 <hr>
""")

#查詢
sql="select id, title,msg, nickname,likes from guestbook order by likes desc;"
cur.execute(sql)
records = cur.fetchall()
for (id,title, msg, nick, likes) in records:
	print(f"<p>編號{id}: 留言人:{nick} 標題:{title} 內容:{msg} 按讚數:{likes}</p>")

print("</body></html>")

