import  streamlit as st
import cv2, numpy as np

st.write("Старт")
image = st.camera_input("Сфокать")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
html_code = """
<p>Что-то</p>
<style>
* {
    font-family: 'Montserrat', sans-serif;
    font-weight: 200;
    color: var(--tg-theme-text-color);
    background: var(--tg-theme-bg-color);
}
}

</style>
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<script>
const tg = window.Telegram.WebApp;
tg.MainButton.show();
tg.MainButton.setText("Оплатить");
alert("Hello from JavaScript!");
</script>
"""

st.markdown(html_code, unsafe_allow_html=True)

if image is not None:
    image = np.array(bytearray(image.read()), dtype=np.uint8)
    cv2_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(cv2_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    st.image(cv2_img)