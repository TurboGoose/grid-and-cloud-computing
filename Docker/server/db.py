import sqlite3

db_name = "data/data.db"

def create_logs_table():
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logs (log TEXT);")
    con.commit()
    con.close()

def save_log(log: str):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute(f"INSERT INTO logs (log) VALUES ('{log}');")
    con.commit()
    con.close()

def get_logs():
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("SELECT log FROM logs;")
    result = [log[0] for log in cur.fetchall()]
    con.commit()
    con.close()
    return result

def truncate_logs_table():
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("DELETE FROM logs;")
    con.commit()
    con.close()
