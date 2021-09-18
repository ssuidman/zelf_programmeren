import config
from os.path import basename
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def send_mail(email, name, name_peer, faculty_peer, email_peer, phone_peer, files=None):
    
    with open("templates/text_template.txt") as f:
        text = f.read().format(name=name,
                               name_peer=name_peer,
                               faculty_peer=faculty_peer,
                               email_peer=email_peer,
                               phone_peer=phone_peer,
                               config_local=config.local,
                               config_platform=config.platform,
                               config_website=config.website,
                               config_registration=config.registration,
                               config_lead=config.lead,
                               config_safety=config.safety,
                               config_feedback=config.feedback,
                               config_style=config.style)
    
    with open("templates/html_template.html") as f:
        html = f.read().format(name=name,
                               name_peer=name_peer,
                               faculty_peer=faculty_peer,
                               email_peer=email_peer,
                               phone_peer=phone_peer,
                               config_local=config.local,
                               config_platform=config.platform,
                               config_website=config.website,
                               config_registration=config.registration,
                               config_lead=config.lead,
                               config_safety=config.safety,
                               config_feedback=config.feedback,
                               config_style=config.style)

    try:
        email_subject = 'Your ' + str(config.platform) + ' Peer in this Week: ' + name_peer
        
        msg = MIMEMultipart()
        msg['To'] = email
        msg['Subject'] = email_subject
        
        content = MIMEMultipart('alternative')
        content.attach(MIMEText(text, 'plain'))
        content.attach(MIMEText(html, 'html'))
        msg.attach(content)
    
        server = smtplib.SMTP(config.smtp, config.port)
        # UM does not require additional AUTH if using VPN
        #server = smtplib.SMTP_SSL(config.smtp, config.port, context=ssl.create_default_context())
        #server.login(config.account, config.password)
        server.sendmail(config.account, email, msg.as_string())
        time.sleep(3)
        
    except Exception as e:
        print(e)
        pass
    
    finally: 
        server.quit()