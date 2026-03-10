import sqlite3


class NoteCreator:
    def __init__(self):
        self.conn = sqlite3.connect("notes.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)"
        )
        self.conn.commit()

    def create_note(self, title, content):
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        self.conn.commit()

    def get_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

    def __del__(self):
        self.close_connection()

    def get_note_by_id(self, note_id):
        self.cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        return self.cursor.fetchone()

    def get_note_by_title(self, title):
        self.cursor.execute("SELECT * FROM notes WHERE title = ?", (title,))
        return self.cursor.fetchone()

    def delete_note_by_id(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM notes")
        self.conn.commit()
