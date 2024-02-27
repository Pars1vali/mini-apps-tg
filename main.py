import  streamlit as st
import streamlit.components.v1 as components
import requests


st.title("Составить оплату")
name = st.text_input("Название покупки")
desciption = st.text_input("Описаниие")
payload = st.text_input("Долнительные парметры")
currency = st.selectbox("Валюта", options=["rub","usd"])

components.html(f"""<!DOCTYPE html>
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
<p>Чтото</p>
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
            {
                "name": {name},
                "desciption": {currency},
                "payload": {payload},
                "currency": {currency}
            }
        );
        console.log("start");
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
</html>""")




