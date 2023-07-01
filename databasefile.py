import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ahana.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clients(cid INT, name TEXT, contact INT, email TEXT, address TEXT, insta TEXT, facebook TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS books(cname TEXT, bname TEXT, language TEXT, online TEXT, paperback TEXT, ppress TEXT, quantity INT, packages TEXT)")
    con.commit


create_db()