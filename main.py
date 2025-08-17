import os
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import FileResponse
from psycopg2.extras import RealDictCursor

# --- Pydantic 模型 (維持不變) ---
class Book(BaseModel):
    title: str
    author: str
    status: str

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    status: Optional[str] = None

# --- FastAPI 應用程式實例 ---
app = FastAPI()

# --- 資料庫連線 ---
# 從環境變數讀取資料庫連線 URL
DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    """建立並返回 PostgreSQL 資料庫連線"""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"資料庫連線錯誤: {e}")
        # 在實際的產品環境中，您可能需要更完善的錯誤處理
        return None

# --- API 端點 (Endpoints) ---

@app.get("/")
async def read_index():
    return FileResponse('index.html')

# 新增書籍 (Write)
@app.post("/books/", status_code=201)
def create_book(book: Book):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="無法連線至資料庫")
    
    # 建立資料表 (如果不存在的話)
    # 這是一個簡單的作法，在第一次執行時會自動建表
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            status VARCHAR(100)
        );
        """)
        conn.commit()

    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        query = "INSERT INTO books (title, author, status) VALUES (%s, %s, %s) RETURNING id"
        cursor.execute(query, (book.title, book.author, book.status))
        new_book_id = cursor.fetchone()['id']
        conn.commit()
    conn.close()
    return {"id": new_book_id, **book.dict()}

# 取得所有書籍
@app.get("/books/")
def read_books():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="無法連線至資料庫")
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM books ORDER BY id ASC")
        books = cursor.fetchall()
    conn.close()
    return books

# 修改書籍資訊 (Update/Rewrite)
@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookUpdate):
    # (這部分為了簡化，暫時省略，您可以之後再補上)
    # 更新的邏輯和 MySQL 類似，但語法可能需要微調
    return {"message": "更新功能尚未實作"}


# 刪除書籍 (Delete)
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="無法連線至資料庫")
    with conn.cursor() as cursor:
        query = "DELETE FROM books WHERE id = %s"
        cursor.execute(query, (book_id,))
        conn.commit()
        affected_rows = cursor.rowcount
    conn.close()
    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="找不到該 ID 的書籍")

    return {"message": f"書籍 ID {book_id} 已成功刪除"}
