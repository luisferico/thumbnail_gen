from fastapi import File, UploadFile, Query, APIRouter
from fastapi.responses import FileResponse, JSONResponse
from .image_functions import thumbnail_based_wh, thumbnail_based_rr, analyze_image

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

router = APIRouter()


@router.post("/analyze_image/")
async def analyze_image_route(file: UploadFile = File(...)):
    # Read the uploaded image
    contents = await file.read()

    # Analyze the image
    image_info = analyze_image(contents)

    return image_info


@router.post("/generate_thumbnail/")
async def generate_thumbnail(
        file: UploadFile = File(...),
        width: int = Query(..., description="Width of the thumbnail."),
        height: int = Query(..., description="Height of the thumbnail.")
    ):
    # Read the uploaded image
    contents = await file.read()

    thumbnail_path, _ = thumbnail_based_wh(contents, width, height)

    # Return the thumbnail as response
    return FileResponse(thumbnail_path)


@router.post("/generate_thumbnail_v2/")
async def generate_thumbnail_v2(
        file: UploadFile = File(...),
        reduction_ratio: float = Query(..., description="Reduction Ratio of the thumbnail.")
    ):
    # Read the uploaded image
    contents = await file.read()

    thumbnail_path, _ = thumbnail_based_rr(contents, reduction_ratio)

    # Return the thumbnail as response
    return FileResponse(thumbnail_path)


@router.post("/metrics_thumbnail/")
async def metrics_thumbnail(
        file: UploadFile = File(...),
        width: int = Query(..., description="Width of the thumbnail."),
        height: int = Query(..., description="Height of the thumbnail.")
    ):
    # Read the uploaded image
    contents = await file.read()

    _, metrics = thumbnail_based_wh(contents, width, height)

    # Return the thumbnail as response
    return {
        "ssi_score": metrics[0],
        "psnr_score": metrics[1]
    }


@router.post("/metrics_thumbnail_v2/")
async def metrics_thumbnail_v2(
        file: UploadFile = File(...),
        reduction_ratio: float = Query(..., description="Reduction Ratio of the thumbnail.")
    ):
    # Read the uploaded image
    contents = await file.read()

    _, metrics = thumbnail_based_rr(contents, reduction_ratio)

    # Return the thumbnail as response
    return {
        "ssi_score": metrics[0],
        "psnr_score": metrics[1]
    }