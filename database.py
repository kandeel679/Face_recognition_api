import sqlite3
import uuid
DATABASE_PATH = "C:\\Users\\youss\\OneDrive\\Desktop\\web_dev_projects\\face_recognition_api\\Database\\facerecognition_database.db"

# Uncomment the following lines to delete all records from the user table
# conn = sqlite3.connect(DATABASE_PATH)
# cur = conn.cursor()
# cur.execute('''DELETE FROM user''')
# conn.close()

def create_user_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    # Creating the user table with id as the primary key
    cur.execute('''CREATE TABLE IF NOT EXISTS user (
                id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                password TEXT
             )''')

    conn.commit()
    conn.close()
def delete():
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    # Creating the user table with id as the primary key
    cur.execute('DROP TABLE IF EXISTS user')

    conn.commit()
    conn.close()

def insert_user(name, email, password):
    if name == '' or email == '' or password == '':
        return None
    user_id = str(uuid.uuid4())

    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    resp = cur.execute('''SELECT * FROM user WHERE email=? AND password=? AND name=?''', (email, password, name))
    ans = resp.fetchone()

    if ans is not None:
        conn.commit()
        conn.close()
        return resp
    else:
        cur.execute('''INSERT OR IGNORE INTO user (id, name, email, password) VALUES (?, ?, ?, ?)''', (user_id, name, email, password))
        conn.commit()
        conn.close()
        return resp

def Check_user(email, password):
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    ans = cur.execute('''SELECT * FROM user WHERE email=? AND password=?''', (email, password))
    result = ans.fetchone()
    conn.close()
    return result

def delete_user_by_email(email):
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    cur.execute('''SELECT email FROM user WHERE email=?''', (email,))
    existing_user = cur.fetchone()

    if existing_user:
        cur.execute('''DELETE FROM user WHERE email=?''', (email,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
def getUserByid(id):
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM user WHERE id=?''', (id,))
    user = cur.fetchone()
    
    conn.close()
    
    
    
    
    
    
    
    
    
    
    
# delete_user_by_email("youssifk000@gmail.com")

# Create the user table if it doesn't exist
# delete()
# create_user_table()
insert_user("ahmed","youssef@GMAIL.XOM","123123")