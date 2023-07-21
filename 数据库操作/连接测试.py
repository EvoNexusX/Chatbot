import pymssql
CONFIG = {
    "host": 'localhost:59784',
    'server': "Owerzhu\MSSQLSERVER02",
    "user": 'sa',
    "pwd": '123456',
}
conn = pymssql.connect(CONFIG['host'],CONFIG['user'], CONFIG['pwd'],charset="UTF-8")
if conn:
    print("服务器链接成功！")
# 创建游标
cursor = conn.cursor()
try:
    conn.autocommit(True)   #指令立即执行，无需等待conn.commit()
    sql = "CREATE DATABASE WORLD "
    cursor.execute(sql)
    conn.autocommit(False) #指令关闭立即执行，以后还是等待conn.commit()时再统一执行
except:
    print("数据库WORLD已经创建！无需重复创建")
conn.close()
# # 创建表
# sql_2 = '''CREATE TABLE `employee` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `topic` INT ,
#   `ptid` INT NOT NULL,
#   `level` INT NOT NULL,
#   `time` TIME,
#   `consume` INT NOT NULL,
#   `err` INT NOT NULL,
#   `points` INT NOT NULL,
#   `gid` INT NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# '''
# cursor.execute(sql_2)
#
conn.close()
