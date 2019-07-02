import smtplib
from email.mime.text import MIMEText
from email.header import Header


class mailhelper(object):
    def __init__(self):

        self.mail_host = 'smtp.qq.com'
        self.mail_user = '82394'
        self.mail_pass = 'vrmnvhk'

    def send_mail(self):
        message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
        message['From'] = Header("Header", 'utf-8')  # 发送者
        message['To'] = Header("C", 'utf-8')  # 接收者
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            sever = smtplib.SMTP()
            sever.connect(self.mail_host,25)
            sever.login(self.mail_user,self.mail_pass)
            sever.sendmail('823942...','2448....',message.as_string())
            sever.close()
            print("发送成功")
        except smtplib.SMTPException:
           print('无法发送')

if __name__ == '__main__' :
        mailhelper().send_mail()
