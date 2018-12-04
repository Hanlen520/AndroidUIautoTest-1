#coding=utf-8

import email
import mimetypes
import os
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from datetime import datetime
from Common import readConfig

#需要加注释


localReadConfig = readConfig.ReadConfig()

'''1. 构造MIMEMultipart对象做为根容器 
2. 构造MIMEText对象做为邮件显示内容并附加到根容器 
3. 构造MIMEBase对象做为文件附件内容并附加到根容器 
　　a. 读入文件内容并格式化 
　　b. 设置附件头 
4. 设置根容器属性 
5. 得到格式化后的完整文本 
6. 用smtp发送邮件 '''

class MyEmail():
    def __init__(self):
        global host,user,password,port,sender,title,content
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")
        self.content = localReadConfig.get_email("content")
        self.value = localReadConfig.get_email("receiver")
        self.receiver = []

        #获取接受者列表
        for n in str(self.value).split("/"):
            self.receiver.append(n)

        #定义邮件标题
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title + " " +date
        # self.log = Log.MyLog()
        # self.logger = self.log.get_log()
        self.msg = MIMEMultipart()
        # print(self.subject)

    # def zipf(self):
        reportpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\"+"Report"
        print('reportpath', reportpath)
        goal_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\" + "Result" + "\\" + "UIautotest-Report"
        shutil.make_archive(goal_path, 'zip', reportpath)
        # list = os.listdir('D:\code\AndroidUIAutotest\kaishu\Result')
        # print('list', list)

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)
        # print('msg to',self.msg['to'])

    def config_content(self, file):
        #需要加注释
        content = self.content + file

        print(content)
        content_plain = MIMEText(content,'plain','utf-8')
        self.msg.attach(content_plain)

    def config_file(self):
        reportpath = os.path.dirname(os.path.abspath(__file__))

        zippath = os.path.join(readConfig.parDir, "Result", "UIautotest-Report.zip")
        file_name =zippath
        print('zippath----',zippath)

        #读取文件流
        data = open(file_name, 'rb')
        ctype, encoding = mimetypes.guess_type(file_name)
        #判断文件类型
        if ctype is None or encoding is not None:
             ctype = 'application/zip'
        maintype, subtype = ctype.split('/', 1)
        # print(maintype,subtype)
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        #设置文件编码
        email.encoders.encode_base64(file_msg)

        #设置附件头
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition', 'attachment', filename=basename)  # 修改邮件头

        self.msg.attach(file_msg)


    def send_email(self,file):
        self.config_header()
        self.config_content(file)
        self.config_file()

        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user,password)
            smtp.sendmail(sender,self.receiver,self.msg.as_string())
            smtp.quit()
            # self.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            print(ex)
            # self.logger.error(str(ex))


# if __name__ == "__main__":
#     print('main')
#     p = MyEmail()
#     # p.zipf()
#     p.send_email()












































