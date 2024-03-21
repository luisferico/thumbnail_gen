import os
import requests
from io import BytesIO
from PIL import Image
import streamlit as st
from utils import set_background

current_dir = os.path.dirname(os.path.abspath(__file__))
temp_dir = os.path.join(current_dir, "temp")
api_url = "thumbnail-load-balancer-318738320.us-east-1.elb.amazonaws.com:8000/"
set_background("./bg/background.jpg")

# Title of the application
st.title("Thumbnail Generator")

# Header
st.header("Please upload a image the you want smaller")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


def save_uploadedfile(uploadedfile):
    with open(os.path.join(temp_dir, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return st.success("Saved File: {} to temp".format(uploadedfile.name))


# If an image is uploaded
if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=False)

    save_uploadedfile(uploaded_file)

    # Send the image to the server for analysis by default
    files = {
        "file": uploaded_file.getbuffer()
    }

    response = requests.request("POST",f"{api_url}analyze_image/", files=files)

    if response.status_code == 200:
        image_info = response.json()
        st.header("Metadata Relevant to the Image")
        st.write("Image Size (KB):", image_info["image_size_KB"])
        st.write("Width:", image_info["width"])
        st.write("Height:", image_info["height"])
        st.write("Metadata:", image_info["metadata"]["0th"])
        st.write("GPS Info:", image_info["metadata"]["GPS"])

        st.header("Thumbnail generated")
        # Option to select thumbnail generation method
        thumbnail_method = st.selectbox("Select thumbnail generation method", ["Reduction Ratio", "Width and Height"])

        if thumbnail_method == "Width and Height":
            width = st.slider("Width", min_value=100, max_value=image_info["width"], step=10,
                              value=int(image_info["width"] / 2))
            height = st.slider("Height", min_value=100, max_value=image_info["height"], step=10,
                               value=int(image_info["height"] / 2))
            # if st.button("Generate Thumbnail"):
            #     thumbnail_response = requests.post(f"http://localhost:8080/generate_thumbnail/?width={width}&height={height}", files=files)
            thumbnail_response = requests.post(
                f"{api_url}generate_thumbnail/?width={width}&height={height}", files=files)

        elif thumbnail_method == "Reduction Ratio":
            reduction_ratio = st.slider("Reduction Ratio", min_value=0.05, max_value=1.0, step=0.05, value=0.5)
            # if st.button("Generate Thumbnail"):
            #     thumbnail_response = requests.post(f"http://localhost:8080/generate_thumbnail_v2/?reduction_ratio={reduction_ratio}", files=files)
            thumbnail_response = requests.post(f"{api_url}generate_thumbnail_v2/?reduction_ratio={reduction_ratio}", files=files)

        if thumbnail_response.status_code == 200:
            thumbnail = Image.open(BytesIO(thumbnail_response.content))
            st.image(thumbnail, caption="Generated Thumbnail", use_column_width=False)

        if st.download_button(
                label="Download image",
                data=thumbnail_response.content,
                file_name="imagename.jpg",
                mime="image/jpg"):

            st.header("Metrics Relevant to the image compression")
            if thumbnail_method == "Width and Height":
                metrics_response = requests.post(f"{api_url}metrics_thumbnail/?width={width}&height={height}", files=files)
            elif thumbnail_method == "Reduction Ratio":
                metrics_response = requests.post(f"{api_url}metrics_thumbnail_v2/?reduction_ratio={reduction_ratio}", files=files)

            if metrics_response.status_code == 200:
                thumbnail_metric = metrics_response.json()
                st.write("SSI (Structural Similarity Index):", thumbnail_metric["ssi_score"])
                st.info("Measures the structural similarity between two images. A value of 1 indicates perfect similarity between the images.")
                st.write("PSNR (Peak Signal-to-Noise Ratio)", thumbnail_metric["psnr_score"])
                st.info("""
                Measures the ratio between the maximum power of a signal (original image) and the power of the noise that degrades it (difference between the original image and the compressed or modified image). Higher values indicate better image quality.
                - 0 to 20 dB: Poor quality
                - 20 to 30 dB: Fair quality
                - 30 to 40 dB: Good quality
                - Above 40 dB: Excellent quality
                    """)

    else:
        st.write('An Error has ocurred!!!')
