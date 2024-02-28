import streamlit as st
from streamlit.components.v1 import html, iframe
import requests, json
from streamlit_qrcode_scanner import qrcode_scanner
from qreader import QReader

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
    qr_code = qrcode_scanner(key='qrcode_scanner')

    if qr_code:
        st.write(qr_code)
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







