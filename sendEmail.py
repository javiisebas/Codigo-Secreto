import os
import smtplib
from os import remove
import base64
from email.message import EmailMessage

def enviaCorreo(correos):
    emisor = 'jsf.codigo.secreto@gmail.com'
    password = 'passwordprueba5'

    messageText = ''' 
    <doctype !html>
    <html>
    <body>
        <h1 style="text-align:center; color:black;">Bienvenido a Código Secreto</h1><br>
        <p style="text-align:justify; color:black;"> Cada jefe de espías dirá en su turno una pista
        compuesta por una sola palabra que puede referirse a varias de las palabras que hay en el 
        tablero. Sus compañeros de equipo intentarán adivinar esas palabras evitando señalar las 
        palabras del equipo rival.</p>
        <h3 style="text-align:center; color:black;">Descargaté el patrón para empezar a jugar<h3>
    </body>
    </html>
    '''

    msg = EmailMessage()
    msg['Subject'] = 'Patrón del juego'
    msg['From'] = emisor
    msg['To'] = correos
    msg.add_alternative(messageText, subtype='html')

    fp =  open('patron.png', 'rb') 
    img_data = fp.read()
    msg.add_attachment(img_data, maintype = 'png',subtype = 'pdf', filename = 'patron.png')

    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(emisor,password)
    mailServer.sendmail(emisor,correos, msg.as_string())
    mailServer.close() 
