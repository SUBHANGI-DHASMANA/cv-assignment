import streamlit as st
import cv2
import numpy as np

def access_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        st.image(frame, channels="BGR")
        if st.button('Stop'):
            break
    cap.release()

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        st.image(frame, channels="BGR")
        if st.button('Stop'):
            break
    cap.release()

def write_video(input_video, output_video):
    cap = cv2.VideoCapture(input_video)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        st.image(frame, channels="BGR")
        if st.button('Stop'):
            break
    cap.release()
    out.release()

def apply_filters():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        
        # Canny edge detection
        edges = cv2.Canny(frame, 100, 200)
        
        # Blur
        blurred = cv2.GaussianBlur(frame, (15, 15), 0)
        
        # Feature detection (using Harris corner detection as an example)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.cornerHarris(gray, 2, 3, 0.04)
        frame[corners > 0.01 * corners.max()] = [0, 0, 255]

        st.image(frame, channels="BGR", caption="Original")
        st.image(edges, caption="Canny Edge Detection")
        st.image(blurred, channels="BGR", caption="Blurred")
        
        if st.button('Stop'):
            break

    cap.release()

def main():
    st.title("OpenCV Streamlit App")

    option = st.sidebar.selectbox("Select Option", ["Access Camera", "Read Video", "Write Video", "Apply Filters"])

    if option == "Access Camera":
        access_camera()
    elif option == "Read Video":
        video_path = st.sidebar.text_input("Enter video path:")
        if st.button("Start"):
            read_video(video_path)
    elif option == "Write Video":
        input_video = st.sidebar.text_input("Enter input video path:")
        output_video = st.sidebar.text_input("Enter output video path:")
        if st.button("Start"):
            write_video(input_video, output_video)
    elif option == "Apply Filters":
        apply_filters()

if __name__ == "__main__":
    main()
