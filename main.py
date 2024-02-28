import streamlit as st
from auth import *

st.camera_input("Сделай фотку")
st.page_link(get_login_str(), label="Войти в Google аккаунт")
if st.button("display user"):
    display_user()
