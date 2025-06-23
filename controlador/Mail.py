import smtplib
import sys, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

class Mail:
    def __init__(self):
        self.server_smtp = os.getenv('SERVER_SMTP')
        self.server_port = os.getenv('SMTP_PORT')
        self.usuario = os.getenv('SMTP_USER')
        self.password = os.getenv('SMTP_PASSWORD')
        self.msg = MIMEMultipart()
        self.detinatario = None
        self.asunto = None
        self.mensaje = None

    def envioMail(self):
        remitente = self.usuario
        self.msg['From'] = remitente
        self.msg['To'] = self.detinatario
        self.msg['Subject'] = self.asunto
        self.msg.attach(MIMEText(self.mensaje, 'plain'))
        
        try:
            server = smtplib.SMTP(self.server_smtp, self.server_port)
            server.ehlo()  
            server.starttls()
            server.ehlo()  
            server.login(self.usuario, self.password)
            texto = self.msg.as_string()
            server.sendmail(remitente, self.detinatario, texto)
            server.quit()
            print("Correo enviado correctamente.")
        except Exception as e:
            print("Error al enviar el correo:", e)       
    
