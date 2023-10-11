from fastapi import APIRouter
from pydantic import BaseModel

from backend.db import connect


class AssignReq(BaseModel):
    staff_id: int

router = APIRouter()

@router.get("/cases")
async def read_cases():
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cases ORDER BY case_status;")
    results = cursor.fetchall()
    return results

@router.post("/cases/{case_id}/assign")
async def assign_therapist(case_id: int, req: AssignReq):
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE cases SET status = 'assigned' where case_id = %s;", (case_id,))

    # check for most recent therapist_case for this case
    cursor.execute("SELECT * FROM therapist_case WHERE case_id = %s ORDER BY updated_at DESC LIMIT 1;", (case_id,))
    most_recent = cursor.fetchone()
    if most_recent is None:
        # a therapist has not yet been added to case
        cursor.execute("INSERT INTO therapist_cases (staff_id, case_id, therapist_status) VALUES (%s, %s, 'assigned');", (req.staff_id, case_id,))
        return {
            "status": "success",
            "message": f"{req.staff_id} successfully added to case {case_id}"
        }

    # the case has had a therapist assigned before check it does not have status of assigned
    if most_recent[2] != 'send back':
        #  report error
        return {
            "status": "failure",
            "message": f"could not assign case {case_id} as it is already assigned."
        }

    # most recent is unassigned
    cursor.execute("INSERT INTO therapist_cases (staff_id, case_id, therapist_status) VALUES (%s, %s, 'assigned');", (req.staff_id, case_id,))
    return {
        "status": "success",
        "message": f"{req.staff_id} successfully added to case {case_id}"
    }


@router.post("/cases/{case_id}/unassign")
async def remove_therapist(case_id: int, req: AssignReq):
    conn = connect.connect_to_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE cases SET status = 'unassigned' where case_id = %s;", (case_id,))
    cursor.execute("UPDATE therapist_cases SET status = 'sent back' where staff_id;", (req.staff_id, case_id,))
    results = cursor.fetchall()
    return results
