import csv
import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("sam111jc@gmail.com", "MY PASSWORD")

msg = "YOUR MESSAGE!"
server.sendmail("sam111jc@gmai.com", "sam111jc@gmail.com", msg)

with open('PythonParseTest.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for person in reader:
        print(person[0])

server.quit()
