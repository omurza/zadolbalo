import sqlite3

def create_tables():
    conn = sqlite3.connect("proba2.0.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        chat_id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        balance INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def register_user(chat_id, full_name):
    conn = sqlite3.connect("proba2.0.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO user (chat_id, full_name) VALUES (?, ?)", (chat_id, full_name))
    conn.commit()
    conn.close()

def get_user_balance(chat_id):
    conn = sqlite3.connect("proba2.0.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM user WHERE chat_id = ?", (chat_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def set_user_balance(chat_id, new_balance):
    conn = sqlite3.connect("proba2.0.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET balance = ? WHERE chat_id = ?", (new_balance, chat_id))
    conn.commit()
    conn.close()

def transfer_money(sender_chat_id, receiver_chat_id, amount):
    conn = sqlite3.connect("proba2.0.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM user WHERE chat_id = ?", (sender_chat_id,))
    sender_balance = cursor.fetchone()
    
    if sender_balance and sender_balance[0] >= amount:
        cursor.execute("UPDATE user SET balance = balance - ? WHERE chat_id = ?", (amount, sender_chat_id))
        cursor.execute("UPDATE user SET balance = balance + ? WHERE chat_id = ?", (amount, receiver_chat_id))
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False
