import streamlit as st
import requests, json
from streamlit.components.v1 import html
# from pyzbar.pyzbar import decode
# # from PIL import Image
# pyzbar==0.1.9
# pillow==10.2.0

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def send(promo_code):
    url = "https://d5dip6pritbe7tmoain3.apigw.yandexcloud.net/aibot"

    headers = {'Content-Type': 'application/json',
               'X-Custom-Info': 'check_promo'}

    data_json = json.dumps({
        'promo_code': promo_code
    })
    response = requests.post(url=url, data=data_json, headers=headers)
    return response.text
qr = st.toggle("Промокод/QR-код")

if qr:
    image = st.camera_input("Сфоткай QR код")
    # html("""<script>alert("f");</script>""")

    if image is not None:
        # decocdeQR = decode(Image.open(image))
        # st.write(decocdeQR[0].data.decode('ascii'))
        st.write("dd")
else:
    promo_code = st.text_input("Промокод")
    send_btn = st.button("Проверить промокод")

    if send_btn:
        if promo_code=="":
            st.warning("Введите промокод")
        else:
            responce = send(promo_code)
            st.caption("Промокод на скидку")
            st.title(f"{responce.split(' ')[1]} - "
                     f"{responce.split(' ')[0]}%")







