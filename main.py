import streamlit as st
st.markdown(
    """
    <div id="div"></div>
     <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script>
    const tg = window.Telegram.WebApp;
    tg.MainButton.show();
    tg.MainButton.setText("Оплатить");
    </script>
    """,
    unsafe_allow_html=True,
)