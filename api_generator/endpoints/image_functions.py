import cv2
import numpy as np
from skimage.metrics import structural_similarity, peak_signal_noise_ratio
import piexif

def thumbnail_based_wh(file_contents: bytes, width: int, height: int):
    """
    Generate a thumbnail of an image based on specified width and height.

    Args:
        file_contents (bytes): The bytes of the image file.
        width (int): The desired width of the thumbnail.
        height (int): The desired height of the thumbnail.

    Returns:
        tuple: A tuple containing the file path to the generated thumbnail and the thumbnail image as a NumPy array.
    """
    nparr = np.frombuffer(file_contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Resize the image to generate the thumbnail
    thumbnail = cv2.resize(img, (width, height))

    # Save the thumbnail to a temporary file
    thumbnail_path = r".\tmp\thumbnail.jpg"
    cv2.imwrite(thumbnail_path, thumbnail)

    return thumbnail_path, (calculate_image_metrics(img, thumbnail))


def thumbnail_based_rr(file_contents: bytes, reduction_ratio: float):
    """
    Generate a thumbnail of an image based on a specified reduction ratio.

    Args:
        file_contents (bytes): The bytes of the image file.
        reduction_ratio (float): The reduction ratio by which to resize the image.

    Returns:
        tuple: A tuple containing the file path to the generated thumbnail and the thumbnail image as a NumPy array.
    """
    nparr = np.frombuffer(file_contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    width = int(img.shape[1] * reduction_ratio)
    height = int(img.shape[0] * reduction_ratio)

    # Resize the image to generate the thumbnail
    thumbnail = cv2.resize(img, (width, height))

    # Save the thumbnail to a temporary file
    thumbnail_path = r".\tmp\thumbnail.jpg"
    cv2.imwrite(thumbnail_path, thumbnail)

    return thumbnail_path, (calculate_image_metrics(img, thumbnail))


def analyze_image(file_contents: bytes):
    """
    Analyze an image and retrieve its size and dimensions.

    Args:
        file_contents (bytes): The bytes of the image file.

    Returns:
        dict: A dictionary containing information about the image, including its size in MB, width, and height.
    """

    # Read image
    nparr = np.frombuffer(file_contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Get image size in bytes
    image_size_bytes = len(cv2.imencode('.jpg', img)[1])

    # Get image dimensions
    height, width, _ = img.shape

    exif_data = piexif.load(file_contents)
    formatted_exif_data = {}
    for ifd, data in exif_data.items():
        formatted_exif_data[ifd] = {}
        if isinstance(data, dict):
            for tag, value in data.items():
                tag_name = piexif.TAGS[ifd][tag]["name"]
                formatted_exif_data[ifd][tag_name] = value
        else:
            del formatted_exif_data[ifd]

    return {
        "image_size_KB": round(image_size_bytes / 1024, 2),
        "width": width,
        "height": height,
        "metadata": formatted_exif_data
    }


def calculate_image_metrics(original_image, reduced_image):
    """
    Calculate the Structural Similarity Index (SSI) and Peak Signal-to-Noise Ratio (PSNR) between two images.

    Args:
        original_image: The original image.
        reduced_image: The reduced image.

    Returns:
        tuple: A tuple containing the SSI score and PSNR score.
    """
    # Resize the reduced image to match the size of the original image
    reduced_image = cv2.resize(reduced_image, (original_image.shape[1], original_image.shape[0]))
    # Convert images to grayscale (if necessary)
    original_image_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    reduced_image_gray = cv2.cvtColor(reduced_image, cv2.COLOR_BGR2GRAY)

    # Calculate Structural Similarity Index (SSI)
    ssi_score, _ = structural_similarity(original_image_gray, reduced_image_gray, full=True)

    # Calculate Peak Signal-to-Noise Ratio (PSNR)
    psnr_score = peak_signal_noise_ratio(original_image, reduced_image)

    return ssi_score, psnr_score
