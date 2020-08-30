import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import globalparam
from common.log import Log


logger = Log()


class SendMail:
    def __init__(self, receiver=None):
        """设置收件人地址"""
        if globalparam.RECEIVE_ADDRESS:
            self.receive_address = globalparam.RECEIVE_ADDRESS
        else:
            self.receive_address = receiver

    def __take_messages(self):
        """生成邮件的内容和html报告附件"""
        self.message = MIMEMultipart()
        self.message["Subject"] = "iDEAS_sit冒烟测试报告"
        self.message["From"] = globalparam.SEND_ADDRESS_NAME
        self.message["Accept-Language"] = "zh-CN"
        self.message["Accept-Charset"] = "ISO-8859-1,utf-8"

        with open(globalparam.TEST_RESULT_PATH, 'rb') as f:
            self.content = f.read()
        self.bodyApart = MIMEText(_text=self.content, _subtype='plain', _charset='utf-8')
        self.message.attach(self.bodyApart)

        with open(globalparam.ALLURE_HTML_PATH, 'rb') as f1:
            self.html = f1.read()
        self.htmlApart = MIMEApplication(self.html)
        self.htmlApart.add_header('Content-Disposition', 'attachment', filename='TestReport.html')
        self.message.attach(self.htmlApart)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        try:
            server = smtplib.SMTP('smtp.163.com')
            server.login(globalparam.SEND_ADDRESS_NAME, globalparam.SEND_ADDRESS_PWD)
            server.sendmail(self.message["From"], self.receive_address, self.message.as_string())
            logger.info("发送邮件成功！")
            server.quit()
        except smtplib.SMTPException as e:
            logger.error('发送邮件失败！')
            logger.info(f'error:\n{e}')
            raise e


if __name__ == '__main__':
    send_mail = SendMail()
    send_mail.send()
