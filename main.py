import streamlit as st
from streamlit.components.v1 import html

html("""
<!DOCTYPE html>
<html lang="en">

<head>
    <script src="https://telegram.org/js/telegram-web-app.js?1"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            font-weight: 200;
            color: var(--tg-theme-text-color);
            background: var(--tg-theme-bg-color);
        }
    </style>
    <title>Document</title>
</head>
<body>
<p>Что-то-x1</p>
<button id="myButton">Нажми меня</button>
    <script>
        document.getElementById("myButton").addEventListener("click", function() {
          alert("Вы нажали кнопку!");
        });        
        Telegram.WebApp.ready();
        
        Telegram.WebApp.MainButton
        .setText('CLOSE WEBVIEW')
        .show()
        .onClick(() => {
            webviewClose();
        });

        
        
        
    </script>
</div>
</body>
</html>
""")

