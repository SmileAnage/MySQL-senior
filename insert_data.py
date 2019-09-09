"""
向数据库插入多条语句
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='country', charset='utf8')

# 获取游标
cur = db.cursor()

name_list = []
for i in range(2000000):
    name = "Tom_{}".format(i)
    print(name)
    name_list.append(name)

sql = 'insert into students (name) values (%s)'  # 创建sql执行语句

# cur.execute(sql, name+list)  # 数据提交频率高，执行速度慢
cur.executemany(sql, name_list)  # 将执行语句合成，一同发送执行，执行效率高

db.commit()

cur.close()
db.close()
