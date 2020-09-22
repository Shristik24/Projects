import sqlite3

class db:
    def __init__(self,datab):
        self.conn=sqlite3.connect(datab)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows=self.cur.fetchall()
        return rows
        
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE books SET title=?,author=?, year=? ,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
    
    def delete(self,id):
        self.cur.execute("DELETE FROM books WHERE id=?",(id,))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()


#connect()
"""insert("ABCD","Shristi",2020,188889)
insert("XYZ","Shristi",2020,18889799)
insert("HELLOW","Simon",1990,1855359)
print(view())
print(search("XYZ"))
update(1,"","Kumari",2020,23288)
delete(3)
print(view())"""