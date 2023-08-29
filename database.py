import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename+ '.db')
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                            title TEXT,
                                            content TEXT NOT NULL);
                    ''')

    def add(self, note):
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO note (title, content) VALUES (?, ?)''', (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cur = self.conn.cursor()
        cursor = cur.execute("SELECT id, title, content FROM note")
        return [(Note(linha[0], linha[1], linha[2])) for linha in cursor]

    def get(self, note_id):
        cur = self.conn.cursor()
        cursor = cur.execute("SELECT id, title, content FROM note WHERE id = ?", (note_id,))
        note = [(Note(linha[0], linha[1], linha[2])) for linha in cursor]
        return note[0]
    
    def update(self, entry):
        cur = self.conn.cursor()
        cur.execute('''UPDATE note SET title = ?, content = ? WHERE id = ?''', (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self,note_id):
        cur = self.conn.cursor()
        cur.execute('''DELETE FROM note WHERE id = ?''', (note_id,))
        self.conn.commit()
