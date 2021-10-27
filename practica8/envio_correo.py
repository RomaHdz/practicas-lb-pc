# Romario Guadalupe Limón Hernández

# Librerias necesarias

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import json
import argparse
import sys



# Creamos los parametros
parser = argparse.ArgumentParser(description="Envio de correos con diferentes funcionalidades")
parser.add_argument("--env", "-e", help="Enviar mensaje", action="store_true")
parser.add_argument("--res", "-r", help="Correr el script (informa si hay un error)", action="store_true")
parser.add_argument("--var", "-v", help="Variable para opcional", default=0)
parser.add_argument("--usr", "-u", help="Usuario o remitente", type=str)
parser.add_argument("--des", "-d", help="Correo del destinatario", type=str, default="enviocorreos0prueba@gmail.com")
parser.add_argument("--pws", "-p", help="Password del usuario o remitente", type=str)

def envio_correo():

    # debemos crear un archivo formato json
    """
    {
        "usr":"correo@algo.obligatorio
        "pws":"contraseña_ultra_duper_secreta"
    }
    """

    with open("datos.json") as f:
        data = json.load(f)

    # Creacion del cuerpo del mensaje
    msg_enviar = MIMEMultipart("alternative")
    msg_enviar["From"] = data["usr"]
    receipents = ["enviocorreos0prueba@gmail.com"]
    msg_enviar["To"] = ", ".join(receipents)
    msg_enviar["Subject"] = "Mensaje de prueba"

    # Este sera el mensaje con estructura html
    html_msg = f"""
    <html>
    <body>
        Hola como te mando este mensaje <i>{data["usr"]}</i><br>
        Si te llego significa que si jalo todo el procedimiento
    </body>
    </html>
    """

    # Especificamos el formato del texto y lo identificamos con nueva variable
    msg_html = MIMEText(html_msg, "html")

    # Adjuntamos el mensaje (msg_html) al curpo del correo
    msg_enviar.attach(msg_html)

    # ************** Parte de enviar el correo *************
    # Se crea un contexto
    context = ssl.create_default_context()
    # Levantamos el servidor
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(data["usr"], data["pws"])
        print("se inicio session")
        server.sendmail(msg_enviar["From"], msg_enviar["To"], msg_enviar.as_string())
        print("Se envio el mensaje")


def correo_resultado(x, usuario, password, destinatario):
    
    try:
        return 1/x

    except (ValueError,TypeError,IndexError,ZeroDivisionError):
        if sys.exc_info()[0] == ValueError:
            mensaje = "de ValueError"
        elif sys.exc_info()[0] == TypeError:
            mensaje = "de TypeError"
        elif sys.exc_info()[0] == IndexError:
            mensaje = "de IndexError"
        elif sys.exc_info()[0] == ZeroDivisionError:
            mensaje = "de ZeroDivisionError"
        else:
            mensaje = "INDEFINIDO"

        # Creamos el cuerpo del correo en caso de que salga todo bien
        msg_enviar = MIMEMultipart("alternative")
        msg_enviar["From"] = usuario
        msg_enviar["To"] = destinatario
        msg_enviar["Subject"] = "Error en la ejecucion"

        html = f"""
        <html>
        <body>
            Hola mi estimado <i>{usuario}</i><br>
            La divicion fue <b>Fallida</b><br>
            El error fue <b>{mensaje}</b>
        </body>
        </html>
        """
        html_msg = MIMEText(html, "html")
        msg_enviar.attach(html_msg)

        context=ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(usuario, password)
            print("Se inicio session")
            server.sendmail(msg_enviar["From"], msg_enviar["To"], msg_enviar.as_string())
            print("Se envio el correo")
            


        




if __name__=='__main__':
    args = parser.parse_args()

    if args.env:
        envio_correo()
    elif args.res:
        correo_resultado(args.var, args.usr, args.pws, args.des)
    else:
        print("Intenta con -h")
