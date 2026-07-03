import sqlite3

def get_connection():
    
    return sqlite3.connect("memory.db")

def init_db():
    
    with get_connection() as connection:
        
        cursor = connection.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            title TEXT
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            role TEXT,
            content TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (session_id) REFERENCES sessions(id)
        ); 
        """)
    
if __name__ == "__main__":
    init_db()