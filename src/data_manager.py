import sqlite3
import pandas as pd
from datetime import datetime
import os

class DataManager:
    def __init__(self, db_path="data/emotions.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.init_database()
    
    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emotions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                emotion TEXT NOT NULL,
                confidence REAL NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_emotion(self, emotion, confidence):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO emotions (emotion, confidence)
            VALUES (?, ?)
        ''', (emotion, confidence))
        
        conn.commit()
        conn.close()
    
    def get_daily_emotions(self, target_date=None):
        if target_date is None:
            target_date = datetime.now().date()
        
        conn = sqlite3.connect(self.db_path)
        
        query = '''
            SELECT * FROM emotions 
            WHERE DATE(timestamp) = ?
            ORDER BY timestamp DESC
        '''
        
        df = pd.read_sql_query(query, conn, params=[target_date])
        conn.close()
        
        return df
