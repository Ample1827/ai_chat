import sqlite3

with sqlite3.connect("memory.db") as connection:
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS sessions(
                    id
                    created_at
                    title   
                   )
                   
                   
                   """)
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS messages(
                    id
                    session_id
                    role
                    content
                    created_at
                   ) 
                   """)
    

# step 1 create new session_id for each new session
# step 2 create messages for session_id
# step 3 while in session_id append each message
