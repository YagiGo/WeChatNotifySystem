DICT = {'User':{'NickName':'Yagi',
        'RemarkName':''},
        'Province':'Beijing'}
print(DICT['User']['RemarkName'] if DICT['User']['RemarkName'] else DICT['User']['NickName'])
import os, sys
dir = os.curdir + '\\Notification Sound\\' + 'Test.txt'
file = open(dir,'r')
print(file)