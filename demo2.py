import re
import requests
from  multiprocessing.dummy import Pool
import time

with open('text.txt','w') as f:
    f.write('')



for i in range(1,10):
    html = requests.get('http://www.jikexueyuan.com/course/?pageNum={}'.format(i))
    title = re.findall('class="lessonimg" title="(.*?)" alt', html.text, re.S)
    content = re.findall('<p style="height: 0px; opacity: 0; display: none;">\n			(.*?)</p>',html.text,re.S)
    with open('text.txt','a') as f:
        for each in title:
            f.write('titles:{}\n'.format(each))
            f.write('content:{}\n'.format(content[title.index(each)]))
            f.write('\n')
    print('正在爬取{}'.format(i))