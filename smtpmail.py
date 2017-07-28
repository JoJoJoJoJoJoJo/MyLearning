import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender='229140959@qq.com'
receiver = 'whr428@163.com'
subject='python test email'
smtpserver='smtp.qq.com'
username='229140959'
password='whr229140959'

msg=MIMEText('Hello,this is a test mail','plain')
msg['Subject']=Header(subject)

smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
