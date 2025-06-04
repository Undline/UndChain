import sqlite3
from typing import Optional

class SimpleSQLiteDB:
    
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS kv_store (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        self.conn.commit()
        self._transaction_active = False

    def put(self, key: str, value: str):
        with self.conn:
            self.conn.execute('''
                INSERT INTO kv_store (key, value) VALUES (?, ?)
                ON CONFLICT(key) DO UPDATE SET value=excluded.value
            ''', (key, value))

    def get(self, key: str) -> Optional[str]:
        cursor = self.conn.execute('SELECT value FROM kv_store WHERE key=?', (key,))
        row = cursor.fetchone()
        return row[0] if row else None

    def delete(self, key: str):
        with self.conn:
            self.conn.execute('DELETE FROM kv_store WHERE key=?', (key,))

    def contains(self, key: str) -> bool:
        cursor = self.conn.execute('SELECT 1 FROM kv_store WHERE key=?', (key,))
        return cursor.fetchone() is not None

    def keys(self):
        cursor = self.conn.execute('SELECT key FROM kv_store')
        return [row[0] for row in cursor.fetchall()]

    def atomic_put(self, key: str, value: str):
        if not self._transaction_active:
            self.conn.execute('BEGIN')
            self._transaction_active = True
        self.conn.execute('''
            INSERT INTO kv_store (key, value) VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value=excluded.value
        ''', (key, value))

    def atomic_commit(self) -> bool:
        if not self._transaction_active:
            return True
        try:
            self.conn.commit()
            self._transaction_active = False
            return True
        except sqlite3.Error:
            self.conn.rollback()
            self._transaction_active = False
            return False

    def close(self):
        if self._transaction_active:
            self.conn.rollback()
        self.conn.close()
