import streamlit as st
from streamlit.components.v1 import html

# # Define your javascript
# my_js = """
# alert("Hola mundo");
# const tg = window.Telegram.WebApp;
# tg.showAlert("Hola!");
# """
#
# # Wrapt the javascript as html code
# my_html = f"<script src=\"tf.js\"></script><script>{my_js}</script>"

# Execute your app
st.title("Javascript example")
# html(my_html)

from static import mycomponent
value = mycomponent(my_input_value="hello there")
st.write("Received", value)