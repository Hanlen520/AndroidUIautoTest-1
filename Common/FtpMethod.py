#coding:utf-8
import os,sys,time
from ftplib import FTP
from Common import readConfig

class FtpMethod(object):


    def __init__(self):
        '''初始化类属性'''
        po = readConfig.ReadConfig()
        self.ip = str(po.get_ftp("ip"))
        self.port = int(po.get_ftp("port"))
        self.user = po.get_ftp("user")
        self.pwd = po.get_ftp("pwd")
        self.localfile = po.get_ftp("local_file")
        self.remotedir = po.get_ftp("remote_dir")

    def connectFtp(self):
        '''连接Ftp服务器'''
        ftp = FTP()
        ftp.set_debuglevel(2)
        ftp.connect(self.ip, self.port)
        ftp.login(self.user, self.pwd)
        ftp.pwd()
        # 打印ftp登录成功后的欢迎提示语
        print(ftp.getwelcome())
        return ftp

    def uploadFtpFile(self):
        '''上传文件'''
        ftp = self.connectFtp()
        print('localfile------',self.localfile)
        fd = open(self.localfile, 'rb')
        # 设置主动模式
        ftp.set_pasv(1)
        # 上传目标文件c
        ftp.storbinary('STOR %s ' % os.path.basename(self.localfile), fd)
        ftp.dir()


    def deleteFtpFile(self, goal_path):
        '''删除文件/目录'''
        ftp = self.connectFtp()
        ftp.cwd(goal_path)
        ftp.dir()
        ftp.rmd("")
        ftp.delete("")
        ftp.rmd("")


#调试用
if __name__ == "__main__":
    fo = FtpMethod()
    fo.connectFtp()
    fo.uploadFtpFile()