from PIL import Image
from io import BytesIO
import requests, json, io, gzip, base64, streamlit as st

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def sendPromoRequest(mode, promo_code):
    url = "https://d5dip6pritbe7tmoain3.apigw.yandexcloud.net/aibot"
    headers = {'Content-Type': 'application/json',
               'X-Custom-Info': 'check_promo'}

    data_json = json.dumps({
        'promo_code': promo_code
    })

    response = requests.post(url=url, data=data_json, headers=headers)
    return response.text
def sendImageServer(image_base64, name):
    url = "https://d5dip6pritbe7tmoain3.apigw.yandexcloud.net/aibot"
    headers = {'Content-Type': 'application/json',
               'X-Custom-Info': 'image_upload'}

    data_json = json.dumps({
        'name': name,
        'photo': image_base64
    })

    response = requests.post(url=url, data=data_json, headers=headers)
    return response.text
def sendRequestNameImges():
    url = "https://d5dip6pritbe7tmoain3.apigw.yandexcloud.net/aibot"
    headers = {'Content-Type': 'application/json',
               'X-Custom-Info': 'get_name_image'}

    response = requests.post(url=url, headers=headers)
    return response.text
def requestImageServer(name):
    url = "https://d5dip6pritbe7tmoain3.apigw.yandexcloud.net/aibot"
    headers = {'Content-Type': 'application/json',
               'X-Custom-Info': 'image_request'}

    data_json = json.dumps({
        'name': name
    })

    response = requests.post(url=url, data=data_json, headers=headers)
    return response.text

qr = st.toggle("Просмотреть/Загрузить")


if qr:
    name_image = st.text_input("Введите название для картинки")
    image = st.camera_input("Сделай фотку")

    if image is not None:
        image_bytes = image.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        st.write(image_base64)
        image_d_base64 = sendImageServer(image_base64, name_image)
        st.write(image_d_base64)

        image_d_bytes = base64.b64decode(image_base64)
        image_d = Image.open(io.BytesIO(image_d_bytes))
        st.image(image_d)

else:
    response = json.loads(sendRequestNameImges())
    if response is not None:
        select_image = st.selectbox("Выбери фотографию", response)
        if select_image is not None:
            st.write(f"Выбранная фотография - {select_image[0]}")
            images_json = json.loads(requestImageServer(select_image[0]))
            image_base64 = images_json[0][0]
            image_data_str = image_base64[2:-1]
            image_data = base64.b64decode(image_data_str)
            image = Image.open(io.BytesIO(image_data))
            st.image(image)

    else:
        st.info("Фотографии не загружены")






