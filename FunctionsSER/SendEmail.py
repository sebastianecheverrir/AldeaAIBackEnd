#Adapted from https://realpython.com/python-send-email/#sending-a-plain-text-email
#https://www.namecheap.com/support/knowledgebase/article.aspx/1179/2175/general-private-email-configuration-for-mail-clients-and-mobile-devices/

from ssl import create_default_context
from smtplib import SMTP_SSL
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def SendEmail(DicInputs):

    EmailAddress = DicInputs['Email']


    ############################################    
    #Create a multipart message
    message = MIMEMultipart()

    ############################################    
    #Set headers

    subject = "Avalúo de tu propiedad"
    sender_email = "contacto@aldea.ai"
    receiver_email = EmailAddress
    password = "AldeaWillSucceed777!!!" #input("Type your password and press enter:")

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    ############################################    
    # Add body to email

    body = "Email/EmailContent.html"
    with open(body) as fp:
        # Create a text/plain message
        message.attach(MIMEText(fp.read(), "html"))

        
    image = MIMEImage(open('Email/cropped-logo.png', 'rb').read())


    ############################################    
    # Add image

    image.add_header('Content-ID', '<image1>')
    message.attach(image)

        
    ############################################    
    # Add pdf as attachment

    # Open PDF file in binary mode

    filename = "Report.pdf"  # In same directory as script

    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message 
    message.attach(part)


    ############################################    
    #  convert message to string

    text = message.as_string()

    ############################################
    # Log in to server using secure context and send email
    context = create_default_context()
    with SMTP_SSL("mail.privateemail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)