from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 解決 CORS 問題，允許 Vue 前端存取
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://todo-app-nu-one-94.vercel.app",  # ← 你的 Vercel 網址
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 暫時用記憶體存資料
todos: list[dict] = [
    {"id": 1, "title": "學習 FastAPI", "done": False},
    {"id": 2, "title": "學習 Vue", "done": False},
]


class TodoCreate(BaseModel):
    title: str


@app.get("/health")
def health_check() -> dict:
    """健康檢查"""
    return {"status": "ok"}


@app.get("/todos")
def get_todos() -> list:
    """取得所有待辦事項"""
    return todos


@app.post("/todos")
def create_todo(todo: TodoCreate) -> dict:
    """新增待辦事項"""
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "done": False,
    }
    todos.append(new_todo)
    return new_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int) -> dict:
    """刪除待辦事項"""
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            return {"message": "刪除成功"}
    raise HTTPException(status_code=404, detail="找不到該待辦事項")
