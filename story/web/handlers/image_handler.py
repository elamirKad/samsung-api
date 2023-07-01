from domain.repositories.image_repository import ImageRepository
from domain.services.image_service import ImageService
from interfaces.schemas.image_schema import ImageCreate, Image
from infrastructure.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()


def get_image_service(db = Depends(get_db)) -> ImageService:
    image_repo = ImageRepository(db=db)
    return ImageService(image_repo=image_repo)


@router.get("/{image_id}", response_model=Image)
def get_audio(
    image_id: int,
    image_service: ImageService = Depends(get_image_service)
):
    image = image_service.get(id=image_id)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return image
