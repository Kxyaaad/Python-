from multiprocessing.dummy import Pool as ThreadPool
import requests
import time

def getsource(url):
    html = requests.get(url)

urls = []


for i in range(1,20):
    newPage = 'http://www.jikexueyuan.com/course/?pageNum={}'.format(i)
    urls.append(newPage)

time1 = time.time()
for i in urls:
    print(i)
    getsource(i)
time2 = time.time()
print('单线程耗时{}'.format(str(time2-time1)))

pool = ThreadPool(4)
time3 = time.time()
result = pool.map(getsource,urls)
pool.close()
pool.join()
time4 = time.time()
print('多线程耗时{}'.format(str(time4-time3)))