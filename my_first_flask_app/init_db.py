import sqlite3
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS messages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visitor_name TEXT NOT NULL,
    visitor_message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
    '''
)


# 提交事务并关闭连接
connection.commit()
connection.close()

print("Database 'messages.db' and table 'messages' created successfully.")