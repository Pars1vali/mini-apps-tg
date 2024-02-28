import streamlit as st
from streamlit.components.v1 import html

html("""
<!DOCTYPE html>
<html lang="en">

<head>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
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
          showPopup();
        });
        
        
        Telegram.WebApp.ready();

        // Event occurs whenever theme settings are changed in the user's Telegram app (including switching to night mode).
        Telegram.WebApp.onEvent('themeChanged', function() {
            document.documentElement.className = Telegram.WebApp.colorScheme;
        });

        // Show main button
        Telegram.WebApp.MainButton.setParams({
            text: 'Main Button'
        });
        Telegram.WebApp.MainButton.onClick(function () {
            Telegram.WebApp.showAlert('Main Button was clicked')
        });	
        Telegram.WebApp.MainButton.show();
        
        function showPopup() {
            Telegram.WebApp.showPopup({
                title: 'Title',
                message: 'Some message',
                buttons: [
                    {id: 'link', type: 'default', text: 'Open ton.org'},
                    {type: 'cancel'},
                ]
            }, function(btn) {
                if (btn === 'link') {
                    Telegram.WebApp.openLink('https://ton.org/');
                }
            });
        };
        
        
        
    </script>
</div>
</body>
</html>
""")

