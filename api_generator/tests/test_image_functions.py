import pytest
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_IMAGE_PATH = os.path.join(TEST_DIR, "test_image_2.png")
# TEST_IMAGE_PATH = os.path.join(TEST_DIR, "test-1920-x-1080.jpg")

project_directory = os.path.abspath(os.path.join(TEST_DIR, ".."))
sys.path.append(project_directory)

from endpoints.image_functions import thumbnail_based_wh, thumbnail_based_rr, analyze_image


def test_thumbnail_based_wh():
    with open(TEST_IMAGE_PATH, "rb") as file:
        file_contents = file.read()

    thumbnail_path, thumbnail = thumbnail_based_wh(file_contents, width=100, height=100)

    assert os.path.exists(thumbnail_path)
    assert thumbnail.shape[:2] == (100, 100)

    os.remove(thumbnail_path)


def test_thumbnail_based_rr():
    with open(TEST_IMAGE_PATH, "rb") as file:
        file_contents = file.read()

    thumbnail_path, thumbnail = thumbnail_based_rr(file_contents, reduction_ratio=0.5)

    assert os.path.exists(thumbnail_path)
    assert thumbnail.shape[:2] == (1440, 2560)

    os.remove(thumbnail_path)


def test_analyze_image():
    # Leer el archivo de prueba
    with open(TEST_IMAGE_PATH, "rb") as file:
        file_contents = file.read()

    # Probar la función analyze_image
    image_info = analyze_image(file_contents)

    # Verificar que la información de la imagen sea correcta
    assert "image_size_MB" in image_info
    assert "width" in image_info
    assert "height" in image_info


if __name__ == "__main__":
    pytest.main()
