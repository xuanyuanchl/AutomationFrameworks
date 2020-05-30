'''To send mail'''

import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib


class SendMail:
    """to send mail"""

    def __init__(self,  file_path):
        file = os.path.join(os.getcwd(), 'MailSender',  'emailJson.json')
        jp = jsonParse()
        jp.loadJson(file)

        # 发送人
        self.from_list = jp.getValue('sender')
        # 收件人['aaa@a.com','bbb@a.com']
        self.to_list = jp.getValue('receivers')
        # 抄送人
        self.copy_list = jp.getValue('cclist')
        # 登录邮件密码base64.encodestring('明文')加密后密码
        self.pass_word = jp.getValue('SMTPAuthenticationCode')
        # 文件具体路径(路径+文件名称)
        self.file_path = file_path
        # 标题头
        self.file_header = jp.getValue('title')
        # 内容
        self.file_body = jp.getValue('content')

    def send(self):
        '''send mail'''
        server = smtplib.SMTP('smtp.qq.com')
        server.starttls()
        # pwd = base64.decodestring(self.pw)
        server.login(self.from_list, self.pass_word)
        try:
            server.sendmail(self.from_list, self.to_list, self.atta())
        finally:
            server.close()

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

class jsonParse:
    data: object = None

    def loadJson(self, file):
        with open(file) as fp:
            import json
            self.data = json.load(fp)
            return self.data

    def getValue(self, key):
        return self.data[key]
