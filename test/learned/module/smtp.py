"""
@Name: smtp.py
@Auth: yingpwu
@Date: 2022/7/21-17:13:37
@Desc:
@Ver : 0.0.0
"""


def smtp():
    from distutils.command.config import config
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    from configparser import ConfigParser
    import os
    # 获取配置文件路径
    root_path = os.path.abspath('.')
    ini_path = os.path.join(str(root_path), 'test/secure/smtp.ini')

    # 获取账号密码
    config = ConfigParser()
    config.read(ini_path)
    account = config.get('mail1', 'account')
    password = config.get('mail1', 'password')
    sendto = config.get('mail1', 'sendto')

    # 创建SMTP对象
    smtpObj = smtplib.SMTP("smtp.qq.com", port=25)  # 默认端口号25

    # 认证信息
    smtpObj.login(account, password)   # 邮箱账户和口令

    # 封装邮件
    message = MIMEText('hello, send by Python...', 'plain', 'utf-8')  # 内容主题
    message['From'] = Header("测试标题", 'utf-8')  # 发件人
    message['To'] = Header("接收测试", "utf-8")   # 收件人
    message['Subject'] = Header('it is a message', 'utf-8')   # 主题

    # 发送邮件
    smtpObj.sendmail(account, sendto, message.as_string())

    # print("发送成功!")

    # import smtplib
    # from email.mime.text import MIMEText
    # from email.mime.multipart import MIMEMultipart
    # from email.header import Header
    #
    # sender = '455303054@qq.com'
    # receivers = ['86413238@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    #
    # # 创建一个带附件的实例
    # message = MIMEMultipart()
    # message['From'] = Header("菜鸟教程", 'utf-8')
    # message['To'] = Header("测试", 'utf-8')
    # subject = 'Python SMTP 邮件测试'
    # message['Subject'] = Header(subject, 'utf-8')
    #
    # # 邮件正文内容
    # message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
    #
    # # 构造附件1，传送当前目录下的 test.txt 文件
    # att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    # message.attach(att1)
    #
    # # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)
    #
    # try:
    #     smtpObj = smtplib.SMTP('localhost')
    #     smtpObj.sendmail(sender, receivers, message.as_string())
    #     print("邮件发送成功")
    # except smtplib.SMTPException:
    #     print("Error: 无法发送邮件")


if __name__ == "__main__":
    smtp()
