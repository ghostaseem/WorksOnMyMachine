from fastapi import APIRouter

from backend.db import connect

router = APIRouter()


# @router.get("/messages")
# async def read_message():
#     conn = connect.connect_to_db()
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM messages")
#     results = cursor.fetchall()
#     return results

@router.get("/chats")
async def read_message():
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chats")
    results = cursor.fetchall()
    return results


@router.get("/chats/{fk_chat_id}")
async def read_message(fk_chat_id: str):
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages WHERE fk_chat_id = %s", (fk_chat_id,))
    results = cursor.fetchall()
    return results