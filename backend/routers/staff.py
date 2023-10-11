from fastapi import APIRouter

router = APIRouter()

staffs=[{"staff_id": "Foo","role":"admin"},{"staff_id":"Bar","role":"Therapist"}]

@router.get("/staffs")
async def read_staffs():
    return staffs

@router.get("/staffs/role/{role}")
async def read_staff_role(role:str):
    return list(filter(lambda staff: staff["role"] == role,staffs))

@router.get("/staffs/staff_id/{staff_id}")
async def read_staff_id(staff_id: str):
    print(staffs)
    print(staff_id)
    return list(filter(lambda staff: staff["staff_id"] == staff_id,staffs))