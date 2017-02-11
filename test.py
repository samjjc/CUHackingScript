import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage

attachment = 'res-1.jpg'

msg = MIMEMultipart()
msg["To"] = 'sam111jc@gmail.com'
msg["From"] = 'sam111jc@gmail.com'
msg["Subject"] = 'test'

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % ('test',attachment), 'html')
msg.attach(msgText)   # Added, and edited the previous line

fp = open(attachment, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("sam111jc@gmail.com", "sjcsjcsjcs")
server.send_message(msg)

print (msg.as_string())
exit(0)