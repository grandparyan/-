from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from typing import Optional
from fastapi.responses import FileResponse # <--- 1. 導入這個

# ... (您的 Book 和 BookUpdate 模型，以及資料庫設定都維持不變) ...

app = FastAPI()

# --- 資料庫連線設定 (維持不變) ---
db_config = {
    # ...
}

# --- API 端點 (Endpoints) ---

# 修改根目錄，讓它回傳你的 HTML 檔案
@app.get("/")
async def read_index():
    # 當使用者瀏覽根目錄時，回傳 index.html 這個檔案
    return FileResponse('index.html')

# ... (您其他的 @app.post, @app.get("/books/"), @app.put, @app.delete 路徑都維持不變) ...