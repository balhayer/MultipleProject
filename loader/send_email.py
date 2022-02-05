import email, smtplib, ssl
from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATE_FORMAT = "%m/%d/%Y"
recipients = ["DL-ADVE.IRV.Web.Tools@wdc.com", "balwinder.hayer@wdc.com"]
# recipients = ["balwinder.hayer@wdc.com", "balwinder.hayer@wdc.com"]
# recipients_cc = ["balwinder.hayer@wdc.com", "balwinder.hayer@wdc.com"]
# recipients_bcc = ["balwinder.hayer@wdc.com", "balwinder.hayer@wdc.com"]


# password = input("Type your password and press enter:")

def send_email(body_content):
    message = MIMEMultipart('alternative')
    message['From'] = 'svc-adveappsvc@wdc.com'
    # message['From'] = 'balwinder.hayer@wdc.com'
    message['To'] = ', '.join(recipients)
    # message['CC'] = ', '.join(recipients_cc)
    message['Subject'] = 'ADVE Sites Validation Report' + " %s" % (date.today().strftime(DATE_FORMAT))
    # message['Bcc'] = ', '.join(recipients_bcc)  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body_content, "html", "utf-8"))
    msg_body = message.as_string()

    # Attachment File
    filename = r"Attachment.html"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        payload = MIMEBase("application", "octet-stream")
        payload.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
    encoders.encode_base64(payload)
    # Add header as key/value pair to attachment part
    payload.add_header("Content-Disposition", "attachment", filename=filename)
    # Add attachment to message and convert message to string
    message.attach(payload)
    msg_body = message.as_string()

    # Server Credentials and Send email
    with smtplib.SMTP("smtp2.wdc.com", 25) as wdc_server:
        wdc_server.sendmail(message['From'], recipients, msg_body)


body_temp = r"Report.html"
with open(body_temp, "r", encoding='utf-8') as file:
    temp = file.read()

if __name__ == '__main__':
    send_email(temp)

# def send_email(msg_body):
# # Add body to email
# message.attach(MIMEText(msg_body, "plain"))
#
# body_temp = "Report.html"
# with open(body_temp, "r", encoding='utf-8') as file:
#     temp = file.read()
#
# # Attachment File
# filename = "Attachment.html"  # In same directory as script
#
# # Open PDF file in binary mode
# with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
# # Encode file in ASCII characters to send by email
# encoders.encode_base64(part)
# # Add header as key/value pair to attachment part
# part.add_header("Content-Disposition", "attachment", filename=filename)
# # Add attachment to message and convert message to string
# message.attach(part)
# msg_body = message.as_string()
#
# # body_temp = "Report.html" # In same directory as script
# # with open(body_temp, "r", encoding='utf-8') as file:
# #     temp = file.read()
# #
# # if __name__ == '__main__':
# #      msg_body(temp)
#
# # Server Credentials and Send email
# with smtplib.SMTP("smtp2.wdc.com", 25) as server:
#     server.sendmail(message['From'], recipients, msg_body)
