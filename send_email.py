
import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import config

def send_mail(send_from, send_to, subject, body_text,smtp):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    body = email.mime.Text.MIMEText(body_text)
    msg.attach(body)

    try:
        fp = open(config.RESUME_FILE_NAME, 'rb')
        att = email.mime.application.MIMEApplication(fp.read(), _subtype="pdf")
        fp.close()
        att.add_header('Content-Disposition', 'attachment', filename=config.RESUME_FILE_NAME)
        msg.attach(att)
    except Exception, e:
        print e
        print "Sent Mail without attachment"

    smtp.sendmail(send_from, send_to, msg.as_string())
    print "Mail Sent to" + send_to