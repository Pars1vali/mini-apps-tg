import streamlit as st
from streamlit.components.v1 import html

# Define your javascript
tg_src = "https://telegram.org/js/telegram-web-app.js"
my_js = """
alert("Hola mundo");
const tg = window.Telegram.WebApp;
tg.MainButton.show();
tg.MainButton.setText("Оплатить");
"""

# Wrapt the javascript as html code
my_html = f"<script src="/{tg_src}/"></script><script>{my_js}</script>"

# Execute your app
st.title("Javascript example")
html(my_html)