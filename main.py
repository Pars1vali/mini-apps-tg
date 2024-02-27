import  streamlit as st
import streamlit.components.v1 as components


st.title("Составить оплату")
name = st.text_input("Название покупки")
desciption = st.text_input("Описаниие")
payload = st.text_input("Долнительные парметры")
currency = st.selectbox("Валюта", options=["rub","usd"])
components.html(



    f"""
    <!DOCTYPE html>
        <html lang="en">

<head>
    <script src="https://telegram.org/js/telegram-web-app.js">
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    }}
    
    body {{
        font-family: 'Montserrat', sans-serif;
        font-weight: 200;
        color: var(--tg-theme-text-color);
        background: var(--tg-theme-bg-color);
    }}
    </style>
    
</head>
<body>
   <script>
   const tg = window.Telegram.WebApp;
    let url = 'https://d5dip6pritbe7tmoain3.apigw.yandexcloud.net/aibot';
    

    tg.MainButton.show();
    tg.MainButton.setText("Оплатить");
    tg.MainButton.onClick(() => {{
        if({name} && {currency} && {payload} && {currency}){{
            tg.showAlert("Заполните все обязательные поля.");
            return;
        }}
        var data = JSON.stringify(
            {{
                "name": {name},
                "description": {currency},
                "payload": {payload},
                "currency": {currency}
            }}
        );
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("X-Custom-Info", "getOpenInvoiceUrl");
        xhr.onreadystatechange = function () {{
            if (xhr.readyState === 4 && xhr.status === 200) {{
                tg.openInvoice(xhr.responseText);
            }}
        }};
        xhr.send(data);
    }});
   </script>
   
</div>
</body>
</html>
""")
image_pic = st.camera_input("Камера мен")
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# image = cv2.imread(image_pic)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2.imshow('Face Detection', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import streamlit as st
#
# # Получение изображения с камеры
# img_file_buffer = st.camera_input("Take a picture")

# Если изображение получено
# if img_file_buffer is not None:
#     # Декодирование изображения с помощью OpenCV
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#
#     # Загрузка предварительно обученного классификатора для детекции лиц
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
#     # Преобразование изображения в оттенки серого (для ускорения процесса детекции)
#     gray_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
#
#     # Поиск лиц на изображении
#     faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Отображение прямоугольников вокруг обнаруженных лиц
#     for (x, y, w, h) in faces:
#         cv2.rectangle(cv2_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#     # Отображение результата
#     st.image(cv2_img, channels="BGR")



