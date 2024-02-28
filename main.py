import streamlit as st
import cv2

image = st.camera_input("Сделайте фотку")

if image is not None:
    st.write("image exists!")
#   image = np.array(bytearray(image.read()), dtype=np.uint8)
#   cv2_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # gray_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)    # faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
    # for (x, y, w, h) in faces:    #     cv2.rectangle(cv2_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # st.image(cv2_img)