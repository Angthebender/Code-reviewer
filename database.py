#going to make a simple database with insert and get functions


import sqlite3

DB_PATH="user_data.db"
#make the file nameed user_data.db


#initialize and create dateabase if it dosent exist
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor =conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS queries(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        
        conn.commit()
    

#inserts into the table above
def save_query(question ,response):
    with sqlite3.connect(DB_PATH) as conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO queries(question,response)VALUES(?,?)",(question,response))
        conn.commit()
        
def get_quesries():
    with sqlite3.connect(DB_PATH) as conn:
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM queries ORDER BY  timestamp DESC")
        return cursor.fetchall()