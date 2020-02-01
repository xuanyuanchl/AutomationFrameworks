'''To send mail'''

import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys
project = r'C:\Users\o5lt\eclipse-workspace\SendMail'  # 项目所在路径
sys.path.append(os.getcwd().split(project)[0] + project)


class SendMail:
    '''to send mail'''

    def __init__(self, From, To, Cc, pw, file_path, file_header, file_body):
        # 发送人
        self.from_list = From
        # 收件人['aaa@a.com','bbb@a.com']
        self.to_list = list(To)
        # 抄送人
        self.copy_list = list(Cc)
        # 登录邮件密码base64.encodestring('明文')加密后密码
        self.pass_word = pw
        # 文件具体路径(路径+文件名称)
        self.file_path = file_path
        # 标题头
        self.file_header = file_header
        # 内容
        self.file_body = file_body

    def send(self):
        '''send mail'''
        server = smtplib.SMTP('smtp.qq.com')
        server.starttls()
        # pwd = base64.decodestring(self.pw)
        server.login(self.from_list, self.pass_word)
        try:
            server.sendmail(self.from_list, self.to_list, self.atta())
        finally:
            server.quit()

    def atta(self):
        '''attach attachment'''
        main_msg = MIMEMultipart()
        # 内容
        text_msg = MIMEText(self.file_body)
        main_msg.attach(text_msg)
        try:
            basename = os.path.basename(self.file_path.split('/')[-1])
            data = open(self.file_path, 'rb')
            file_msg = MIMEApplication(data.read())
            #file_msg = MIMEBase('text', 'html', filename=basename)
            file_msg.add_header('Content-Disposition',
                                'attachment', filename=basename)
            # file_msg.set_payload(data.read())
            data.close()
            # email.encoders.encode_base64(file_msg)

            main_msg.attach(file_msg)
        except Exception as err_exception:
            print(err_exception)

        main_msg['From'] = self.from_list
        main_msg['To'] = ";".join(self.to_list)
        main_msg['Cc'] = ";".join(self.copy_list)

        # 标题头c
        main_msg['Subject'] = self.file_header
        main_msg['Date'] = email.utils.formatdate()

        full_text = main_msg.as_string()

        return full_text


if __name__ == '__main__':
    MAIL_PASS = "xxmyrwzexgiibdhb"  # 密码(这里的密码不是登录邮箱密码，而是授权码)
    CONTENT = 'Python Send Mail !'
    TITLE = 'Python SMTP Mail Test'  # 邮件主题
    ATTACHMENT = r"D:\GitGUI\SeleniumPythonFramework\src\TestResult\0130_221636\Plan1\Plan1.html"
    SENDER = '616191459@qq.com'  # 发件人邮箱
    RECEIVERS = ['616191459@qq.com']  # 接收人邮箱
    S = SendMail(SENDER, RECEIVERS, [], MAIL_PASS, ATTACHMENT, TITLE, CONTENT)
    S.send()
