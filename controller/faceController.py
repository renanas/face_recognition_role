from fastapi import APIRouter

router = APIRouter()


@router.post("/face")
def insert_image():
    return {"faceInclude": "Hello U!"}

@router.get("/face")
def validate_person():
    return {"faceValidation": "YOU SHALL NOT PASS!"}