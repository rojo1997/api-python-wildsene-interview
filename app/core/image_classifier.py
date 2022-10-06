"""Image classfier module"""
from enum import Enum
from typing import Dict, List
from keras import layers
from keras.losses import SparseCategoricalCrossentropy
from keras.models import Sequential
import numpy as np

IMAGE_HEIGHT: int = 256
IMAGE_WIDTH: int = 256


class Classes(str, Enum):
    """Prediction classes"""

    BARE: str = "bare"
    CROPS: str = "crops"
    FOREST: str = "forest"
    WATER: str = "water"


class ImageClassifier:
    """Class to manage model loading and predictions"""

    def __init__(self):
        self.model = self.create_model()
        self.scaler = self.create_scaler()
        self.mask: Dict[str, Classes] = {
            0: Classes.BARE,
            1: Classes.CROPS,
            2: Classes.FOREST,
            3: Classes.WATER,
        }

    def create_model(self) -> Sequential:
        """Create a classification deep learning model.

        Returns:
            Sequential: The model instance.
        """
        model = Sequential(
            [
                layers.Input((IMAGE_HEIGHT, IMAGE_WIDTH, 3)),
                layers.Conv2D(16, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(32, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(64, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Flatten(),
                layers.Dense(128, activation="relu"),
                layers.Dense(len(Classes)),
            ],
        )

        model.compile(
            optimizer="adam",
            loss=SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

        return model

    def create_scaler(self) -> layers.Rescaling:
        """Create a TF scaler to get images values between 0 and 1."""
        return layers.Rescaling(1.0 / 255, input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))

    def load_model(self, path: str):
        """Load pre training weights

        Args:
            path (str): filename
        """
        self.model.load_weights(path)

    def predict_image(self, array: np.ndarray) -> Classes:
        """Predict label for an input image

        Args:
            array (np.ndarray): array image

        Returns:
            Classes: label
        """
        prediction = self.model.predict(
            self.scaler.call(array.reshape(1, IMAGE_HEIGHT, IMAGE_WIDTH, 3))
        )[0]
        return self.mask[np.argmax(prediction)]

    def predict_batch(self, array: np.ndarray) -> List[Classes]:
        """Predict label for multiple images

        Args:
            array (np.ndarray): array images

        Returns:
            List[Classes]: Label list
        """
        index_label: np.ndarray = np.argmax(self.model.predict(
            self.scaler.call(array)
        ), axis = 1)
        return [self.mask[index] for index in index_label]