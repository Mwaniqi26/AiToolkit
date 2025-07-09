import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

st.set_page_config(page_title="MNIST Digit Classifier", layout="centered")

# Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mnist_model.h5")

model = load_model()

# Title and Description
st.title("🖊️ MNIST Digit Classifier")
st.markdown("Upload a **handwritten digit image (0–9)** and this app will predict what digit it is.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")  # convert to grayscale
    image = ImageOps.invert(image)  # invert for white digit on black background

    # Resize to 28x28
    image = image.resize((28, 28))
    image_array = np.array(image)

    # Normalize and reshape
    image_array = image_array / 255.0
    image_array = image_array.reshape(1, 28, 28, 1)

    # Show image
    st.image(image, caption="Uploaded Digit", width=150)

    # Predict
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)

    st.markdown(f"### 🔢 Predicted Digit: **{predicted_digit}**")
