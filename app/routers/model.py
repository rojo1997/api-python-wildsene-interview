"""Hello name module"""
from typing import List
from fastapi import APIRouter, File
from starlette.requests import Request
from pydantic import BaseModel
import numpy as np

from core import (
    Classes, 
    ImageClassifier,
    IMAGE_HEIGHT, 
    IMAGE_WIDTH,
    bytes_to_array
)

router = APIRouter(prefix="", tags=["model"])


class PredictionOutput(BaseModel):
    """Prediction Output Schema"""

    class_: Classes

    class Config:
        fields = {"class_": "class"}


@router.post("/prediction", response_model=PredictionOutput)
async def post_prediction(request: Request, image: bytes = File()) -> str:
    """Endpoint to return prediction result

    Args:
        image (bytes): image to be classified

    Returns:
        str: concatenate string
    """
    array: np.ndarray = bytes_to_array(image)
    image_classifier: ImageClassifier = request.app.state.image_classifier
    return {"class": image_classifier.predict_image(array)}


@router.post("/batch", response_model=List[PredictionOutput])
async def post_batch(request: Request, batch: List[bytes] = File()) -> str:
    """Endpoint to return prediction result

    Args:
        image (bytes): image to be classified

    Returns:
        str: concatenate string
    """
    array: np.ndarray = np.zeros((len(batch),IMAGE_HEIGHT, IMAGE_WIDTH, 3))
    for i in range(len(batch)):
        array[i] = bytes_to_array(batch[i])
    image_classifier: ImageClassifier = request.app.state.image_classifier
    result = image_classifier.predict_batch(array)
    return [{"class": r} for r in result]