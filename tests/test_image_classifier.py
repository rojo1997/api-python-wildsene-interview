"""Test image classfier"""
import sys
from decouple import config
from fastapi.testclient import TestClient

sys.path.append("./app")

from app.main import app
from app.core import (
    ImageClassifier,
    Classes,
    load_image,
    array_to_bytes,
)


def test_2():
    """Test 2: scene classification.

    Should return a dict like this:
    {'class': 'predicted_class'}
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    image = load_image("./data/water/0.jpg")
    image_bytes = array_to_bytes(image)
    files = {"image": image_bytes}
    response = client.post(url="/prediction", files=files)
    assert response.ok, str(response.json())
    assert response.json() == {"class": Classes.WATER}


def test_3():
    """Test 3: scene classification.

    Should return a dict like this:
    {'class': 'predicted_class'}
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    image = load_image("./data/bare/0.jpg")
    image_bytes = array_to_bytes(image)
    files = {"image": image_bytes}
    response = client.post(url="/prediction", files=files)
    assert response.ok, str(response.json())
    assert response.json() == {"class": Classes.BARE}


def test_4():
    """Test 4: scene classification.

    Should return a dict like this:
    {'class': 'predicted_class'}
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    image = load_image("./data/forest/0.jpg")
    image_bytes = array_to_bytes(image)
    files = {"image": image_bytes}
    response = client.post(url="/prediction", files=files)
    assert response.ok, str(response.json())
    assert response.json() == {"class": Classes.FOREST}


def test_5():
    """Test 5: scene classification.

    Should return a dict like this:
    {'class': 'predicted_class'}
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    image = load_image("./data/crops/0.jpg")
    image_bytes = array_to_bytes(image)
    files = {"image": image_bytes}
    response = client.post(url="/prediction", files=files)
    assert response.ok, str(response.json())
    assert response.json() == {"class": Classes.CROPS}


def test_6():
    """Test 6: scene classification.

    Should return a dict like this:
    {'class': 'predicted_class'}
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    image = load_image("./data/forest/1.jpg")
    image_bytes = array_to_bytes(image)
    files = {"image": image_bytes}
    response = client.post(url="/prediction", files=files)
    assert response.ok, str(response.json())
    assert response.json() == {"class": Classes.FOREST}


def test_7():
    """Test 7: Batch scene classification.

    Should return a list of dicts like this:
    [
        {'class': 'predicted_class'},
        {'class': 'predicted_class_2'},
    ]
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    images_paths = [
        "./data/water/1.jpg",
        "./data/crops/1.jpg",
    ]
    images = [load_image(image_path) for image_path in images_paths]
    bytes_list = [array_to_bytes(image) for image in images]
    files = [("batch", image_bytes) for image_bytes in bytes_list]
    response = client.post(url="/batch", files=files)
    assert response.ok, str(response.json())
    assert response.json() == [
        {"class": Classes.WATER},
        {"class": Classes.CROPS},
    ]


def test_8():
    """Test 8: Batch scene classification.

    Should return a list of dicts like this:
    [
        {'class': 'predicted_class'},
        {'class': 'predicted_class_2'},
    ]
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    images_paths = [
        "./data/bare/1.jpg",
        "./data/crops/1.jpg",
        "./data/crops/2.jpg",
    ]
    images = [load_image(image_path) for image_path in images_paths]
    bytes_list = [array_to_bytes(image) for image in images]
    files = [("batch", image_bytes) for image_bytes in bytes_list]
    response = client.post(url="/batch", files=files)
    assert response.ok, str(response.json())
    assert response.json() == [
        {"class": Classes.BARE},
        {"class": Classes.CROPS},
        {"class": Classes.CROPS},
    ]

def test_9():
    """Test 9: Batch scene classification.

    Should return a list of dicts like this:
    [
        {'class': 'predicted_class'},
        {'class': 'predicted_class_2'},
    ]
    """
    app.state.image_classifier = ImageClassifier()
    app.state.image_classifier.load_model(
        path=config("WEIGHTS_PATH", cast=str, default="weights/weights")
    )
    client = TestClient(app)
    images_paths = [
        "./data/water/1.jpg",
        "./data/forest/2.jpg",
        "./data/bare/1.jpg",
    ]
    images = [load_image(image_path) for image_path in images_paths]
    bytes_list = [array_to_bytes(image) for image in images]
    files = [("batch", image_bytes) for image_bytes in bytes_list]
    response = client.post(url="/batch", files=files)
    assert response.ok, str(response.json())
    assert response.json() == [
        {"class": Classes.WATER},
        {"class": Classes.FOREST},
        {"class": Classes.BARE},
    ]