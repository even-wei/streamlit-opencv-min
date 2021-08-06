import streamlit as st
import cv2
import tempfile

file = st.file_uploader("Upload file")
if file:
    # Save file temporarily
    tmpFile = tempfile.NamedTemporaryFile(delete=False)
    tmpFile.write(file.read())

    # Retrieve
    video = cv2.VideoCapture(tmpFile.name)
    stframe = st.empty()

    while video.isOpened():
        ret, frame = video.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        stframe.image(gray)
