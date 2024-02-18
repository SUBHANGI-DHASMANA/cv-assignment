import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Processor")

    st.sidebar.title("Upload Image")
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

        st.sidebar.image(image, caption="Original Image", use_column_width=True)

        st.sidebar.title("Select Operations")
        options = st.sidebar.multiselect("Choose operations:", ["Original", "Convert to Grayscale", "Convert to Binary", "Brightness and Contrast Adjustment"])

        processed_image = image.copy()

        if "Original" in options:
            options = ["Original"]
        else:
            if "Convert to Grayscale" in options:
                processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
            
            if "Convert to Binary" in options:
                gray_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
                _, processed_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
            
            if "Brightness and Contrast Adjustment" in options:
                alpha = st.sidebar.slider("Contrast (1.0-3.0)", 1.0, 3.0, 1.0)
                beta = st.sidebar.slider("Brightness (0-100)", 0, 100, 0)
                processed_image = cv2.convertScaleAbs(processed_image, alpha=alpha, beta=beta)

        st.sidebar.title("Annotation")
        annotation_option = st.sidebar.selectbox("Choose annotation type:", ["None", "Line", "Rectangle", "Circle", "Text"])

        if annotation_option != "None":
            if annotation_option == "Line":
                draw_line(processed_image)
            elif annotation_option == "Rectangle":
                draw_rectangle(processed_image)
            elif annotation_option == "Circle":
                draw_circle(processed_image)
            elif annotation_option == "Text":
                draw_text(processed_image)

        st.image(processed_image, caption="Processed Image", use_column_width=True)

def draw_line(image):
    start_x = st.sidebar.slider("Start X", 0, image.shape[1], 0)
    start_y = st.sidebar.slider("Start Y", 0, image.shape[0], 0)
    end_x = st.sidebar.slider("End X", 0, image.shape[1], image.shape[1])
    end_y = st.sidebar.slider("End Y", 0, image.shape[0], image.shape[0])
    color = st.sidebar.color_picker("Line Color", "#FF5733")
    color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    thickness = st.sidebar.slider("Thickness", 1, 10, 1)
    cv2.line(image, (start_x, start_y), (end_x, end_y), color, thickness)


def draw_rectangle(image):
    start_x = st.sidebar.slider("Top Left X", 0, image.shape[1], 0)
    start_y = st.sidebar.slider("Top Left Y", 0, image.shape[0], 0)
    width = st.sidebar.slider("Width", 1, image.shape[1], image.shape[1] // 2)
    height = st.sidebar.slider("Height", 1, image.shape[0], image.shape[0] // 2)
    color = st.sidebar.color_picker("Rectangle Color", "#FF5733")
    color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    thickness = st.sidebar.slider("Thickness", 1, 10, 1)
    cv2.rectangle(image, (start_x, start_y), (start_x + width, start_y + height), color, thickness)

def draw_circle(image):
    center_x = st.sidebar.slider("Center X", 0, image.shape[1], image.shape[1] // 2)
    center_y = st.sidebar.slider("Center Y", 0, image.shape[0], image.shape[0] // 2)
    radius = st.sidebar.slider("Radius", 1, min(image.shape[1], image.shape[0]) // 2, min(image.shape[1], image.shape[0]) // 4)
    color = st.sidebar.color_picker("Circle Color", "#FF5733")
    color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    thickness = st.sidebar.slider("Thickness", 1, 10, 1)
    cv2.circle(image, (center_x, center_y), radius, color, thickness)

def draw_text(image):
    text = st.sidebar.text_input("Text", "Enter text here")
    position_x = st.sidebar.slider("Position X", 0, image.shape[1], 0)
    position_y = st.sidebar.slider("Position Y", 0, image.shape[0], 0)
    font_scale = st.sidebar.slider("Font Scale", 0.1, 3.0, 1.0)
    color = st.sidebar.color_picker("Text Color", "#FF5733")
    color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    thickness = st.sidebar.slider("Thickness", 1, 10, 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (position_x, position_y), font, font_scale, color, thickness)

if __name__ == "__main__":
    main()
