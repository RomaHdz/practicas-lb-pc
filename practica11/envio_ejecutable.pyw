# Romario Guadalupe Limón Hernández

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
# import json

# with open(ruta) as f:
    # data = json.load(f)

user = "enviocorreos0prueba@gmail.com"
pasw = "correos3434"


msg_enviar = MIMEMultipart("alternative")
msg_enviar["From"] = user
receipents = ["enviocorreos0prueba@gmail.com"]
msg_enviar["To"] = ", ".join(receipents)
msg_enviar["Subject"] = "Funciono el ejecutable"

html = f"""
<html>
<body>
    Que tal <i>{msg_enviar["To"]}</i><br>
    Este mensaje lo recibes desde un <b>ejecutable</b>
</body>
</html>
"""

msg_html = MIMEText(html, "html")
msg_enviar.attach(msg_html)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(user, pasw)
    print("Se inicio session correctamente...")
    server.sendmail(msg_enviar["From"], msg_enviar["To"], msg_enviar.as_string())
    print("Se envio el mail con exito!!")
