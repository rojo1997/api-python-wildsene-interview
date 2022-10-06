"""Utils module, containing image helper functions."""

import io

import numpy as np
from PIL import Image


def show_image(image_path: str) -> None:
    """Show an image in a new window.

    Args:
        image_path (str): The path of the image to be shown.

    Returns:
        None
    """
    image = Image.open(image_path)
    image.show()


def load_image(image_path: str) -> np.array:
    """Load an image from a file.

    Args:
        image_path (str): The path to the image to load.

    Returns:
        np.array: A numpy array containing the loaded image data.
    """
    image = Image.open(image_path)
    return np.array(image)


def array_to_bytes(x: np.ndarray) -> bytes:
    """Convert a numpy array into a bytes representation.

    Args:
        x (np.ndarray): The numpy array to convert.

    Returns:
        bytes: The bytes representation of the numpy array.
    """
    np_bytes = io.BytesIO()
    np.save(np_bytes, x, allow_pickle=True)
    return np_bytes.getvalue()


def bytes_to_array(b: bytes) -> np.ndarray:
    """Convert a bytes array to a numpy array.

    Args:
        b (bytes): The bytes to convert.

    Returns:
        np.ndarray: The resulting numpy array.
    """
    np_bytes = io.BytesIO(b)
    return np.load(np_bytes, allow_pickle=True)
