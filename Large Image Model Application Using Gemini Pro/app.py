# app.py
import streamlit as st
from PIL import Image
from vision import get_gemini_response, process_image

# Title of the web app
st.title("Image Processing with Google Gemini")

# File uploader widget for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Process uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")

    # Input for the question
    question = st.text_input("Ask a question about the image:")

    # Button to process the image and get the answer
    if st.button('Get Answer'):
        if question:
            st.write("Processing your question...")
            # Process image and get answer
            processed_image = process_image(image)
            answer = get_gemini_response(question, processed_image)
            st.subheader("The Response is")
            st.write(answer)
        else:
            st.warning("Please enter a question to get an answer.")
