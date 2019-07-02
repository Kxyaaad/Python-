import requests
import json
from lxml import  etree
from multiprocessing.dummy import Pool as ThreadPool

def towrite(contentDict):
    f.writelines('回帖时间'+str(contentDict['topic_reply_time'])+'\n')
    f.writelines('回帖时间' + str(contentDict['topic_reply_time']) + '\n')
    f.writelines('回帖时间' + str(contentDict['topic_reply_time']) + '\n')
