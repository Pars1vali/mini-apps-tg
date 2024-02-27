import  streamlit as st
import streamlit.components.v1 as components
import requests


st.title("Составить оплату")
name = st.text_input("Название покупки")
desciption = st.text_input("Описаниие")
payload = st.text_input("Долнительные парметры")
currency = st.selectbox("Валюта", options=["rub","usd"])
components.html(f"""
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
    
        tg.showAlert("Тест");

    tg.MainButton.show();
    tg.MainButton.setText("Оплатить");
    tg.MainButton.onClick(() => {{
        tg.showAlert("Тест");
    }});
   </script>
   
</div>
</body>
</html>
""")




