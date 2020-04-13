import smtplib
import email,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from analysis import *
from barcharts import *
from analysis2 import *


def send_email(text,text1):
    subject="Check out my Proyect 2: Data Pipeline!"
    body = """\
    Hola,
    Adjunto vas a encontrar una gráfica con los 10 tenistas con mejores resultados en el torneo y año que seleccionado.
    Además, estos son los ganadores de Grand Slams de los últimos años (2017,2018,2019) con el número total de titulos(Round), media de juegos por partido y media de sets jugados: {text}
    Por último,estos son los datos personales de cada ganador: Nacionalidad, Fecha de Nacimiento, Altura, Ganancias: {text1}
    """
    sender_email = input("Enter sender_email:")
    receiver_email = input("Enter destinatary_email:")
    password = input("Enter password:")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    filename = "Top 10 players.png"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)




