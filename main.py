import csv
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


attachment = "res-1.jpg"
msg = MIMEMultipart()
msg['Subject'] = 'The contents'
msg['From'] = "sam111jc@gmail.com"
msg['To'] = "sam111jc@gmail.com"

msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:img1"><br>Nifty!', 'html')
msg.attach(msgText)
#s = smtplib.SMTP('localhost')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("sam111jc@gmail.com", "sjcsjcsjcs")
server.send_message(msg)


fp = open(attachment, 'r')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<img1>')
msg.attach(msgImage)
#img.add_header('Content-ID', '<{}>'.format(attachment))
#msg.attach(img)


#msg = "YOUR MESSAGE!"
#server.sendmail("sam111jc@gmail.com", "sam111jc@gmail.com", msg)

with open('PythonParseTest.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for person in reader:
        print(person[0])

server.quit()
#s.quit()