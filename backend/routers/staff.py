from fastapi import APIRouter

from backend.db import connect

router = APIRouter()


@router.get("/staff")
async def read_staff():
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM staff")
    results = cursor.fetchall()
    return results

@router.get("/staff/role/{role}")
async def read_staff_role(role:str):
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM staff WHERE staff_role = %s", (role,))
    results = cursor.fetchall()
    return results

@router.get("/staff/staff_id/{staff_id}")
async def read_staff_id(staff_id: str):
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM staff WHERE staff_id = %s", (staff_id,))
    results = cursor.fetchone()
    return results
