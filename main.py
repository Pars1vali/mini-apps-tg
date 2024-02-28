import streamlit as st
from streamlit.components.v1 import html
from streamlit_javascript import st_javascript

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


st.subheader("Javascript API call")

return_value = st_javascript("""
const telegramWebApp = require('https://telegram.org/js/telegram-web-app.js');
telegramWebApp.showAlert("d");
}) """)

st.markdown(f"Return value was: {return_value}")
print(f"Return value was: {return_value}")


st.title("Javascript example")
# html(my_html)
