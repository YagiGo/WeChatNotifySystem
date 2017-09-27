# coding UTF-8

# Created by Yagi
# Version 1.0.1 2017/09/17
#   Basic Structure Finished
#   Receive Message, Audio, Video, Attachment
#   Identify User with NickName or RemarkName, always showing RemarkName if any.
# Version 1.0.2 2017/09/18
#   Support Group Chat!
from itchat.content import *
import itchat, time, os, sys
@itchat.msg_register([TEXT], isFriendChat = True, isGroupChat = True)
def get_response(msg):
    if(msg['Type'] == TEXT):
        print("用户ID为{}".format(msg['User']['RemarkName'] if msg['User']['RemarkName'] else msg['User']['NickName'])
                    + '的好友于'
                    +time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    +'给你发了一条新信息，内容:' + msg['Text'])
@itchat.msg_register([PICTURE, RECORDING, VIDEO, ATTACHMENT])

# 附件储存命名方式：用户ID+附件名称
def get_file(msg):
    if(msg['Type'] == PICTURE):
        msg.download(os.curdir + '\\Image Files\\' + '{}'.format(msg['User']['RemarkName']
                                                                 if msg['User']['RemarkName']
                                                                 else msg['User']['NickName']) + msg['FileName'])
        print("{}于".format(msg['User']['RemarkName'] if msg['User']['RemarkName'] else msg['User']['NickName'])
              + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
              "发给了你一张图片, 名为{}，已保存至根目录".format(msg['FileName']))
    if(msg['Type'] == RECORDING):
        msg.download(os.curdir + '\\Audio Files\\' +  '{}'.format(msg['User']['RemarkName']
                                                                 if msg['User']['RemarkName']
                                                                 else msg['User']['NickName']) + msg['FileName'])
        print("{}于".format(msg['User']['RemarkName'] if msg['User']['RemarkName'] else msg['User']['NickName'])
              + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
              "发给了你一段音频, 名为{}，已保存至根目录".format(msg['FileName']))
    if(msg['Type'] == VIDEO):
        msg.download(os.curdir + '\\Video Files\\' + '{}'.format(msg['User']['RemarkName']
                                                                 if msg['User']['RemarkName']
                                                                 else msg['User']['NickName']) + msg['FileName'])
        print("{}于".format(msg['User']['RemarkName'] if msg['User']['RemarkName'] else msg['User']['NickName'])
              + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
              "发给了你一段视频, 名为{}，已保存至根目录".format(msg['FileName']))
    if(msg['Type'] == ATTACHMENT):
        msg.download(os.curdir + '\\Attachment\\' + '{}'.format(msg['User']['RemarkName']
                                                                 if msg['User']['RemarkName']
                                                                 else msg['User']['NickName']) + msg['FileName'])
        print("{}于".format(msg['User']['RemarkName'] if msg['User']['RemarkName'] else msg['User']['NickName'])
              + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
              "发给了你一个附件, 名为{}，已保存至根目录".format(msg['FileName']))
itchat.auto_login()
itchat.run()
