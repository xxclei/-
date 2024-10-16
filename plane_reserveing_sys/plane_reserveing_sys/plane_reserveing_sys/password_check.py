from django.db import connection

def passwordcheck(username, password):
    # 检查数据库连接
    check_database_connection()
    cursor = connection.cursor()
    # 使用参数化查询来防止 SQL 注入
    cursor.execute("SELECT user_type FROM `user` WHERE username = %s AND password = %s", (username, password))
    rows = cursor.fetchall()

    # 关闭游标
    cursor.close()

    # 检查是否有匹配的行
    if rows:
        # 如果有匹配的行，返回查找成功和用户类型
        user_type = rows[0][0]  # 假设所有匹配的行的用户类型都是一样的
        return True, user_type
    else:
        # 如果没有匹配的行，返回查找失败
        return False,0
        

def check_database_connection():
    try:
        # 尝试执行一个简单的查询
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        print("数据库连接成功。")
    except Exception as e:
        print(f"数据库连接失败：{e}")
    finally:
        if cursor:
            cursor.close()