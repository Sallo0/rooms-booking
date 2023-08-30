import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import resize_image

router = APIRouter(
    prefix="/images",
    tags=["Images"]
)


@router.post("/hotels")
async def upload_hotel_image(file: UploadFile, name: int):
    path = f"app/static/images/{name}.webp"
    with open(path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    resize_image.delay(path, (200, 200))
    return {"filename": file.filename}
