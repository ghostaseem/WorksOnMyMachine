from fastapi import APIRouter

from backend.db import connect

router = APIRouter()


@router.get("/messages")
async def read_message():
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")
    results = cursor.fetchall()
    return results

@router.get("/chats/{chat_id}")
async def read_message(chat_id: str):
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chats WHERE chat_id = %s", (chat_id,))
    results = cursor.fetchall()
    return results