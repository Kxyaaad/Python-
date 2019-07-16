import requests
from bs4 import BeautifulSoup
# url = 'https://movie.douban.com/top250'

urls = ['https://movie.douban.com/top250?start='+str(n)+'&filter=' for n in range(0,250,25)]
print(urls)

for url in urls :
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.content,'html.parser')


    titles = soup.select('div.hd > a') # 标题

    rates = soup.select('span.rating_num') # 评分

    image_urls = soup.select('img[width="100"]') #图片地址

    i = 1
    for title,rate,image_url in zip(titles,rates,image_urls):

        data = {
            'title':list(title.stripped_strings),
            'rate':list(rate),
            'image_url':image_url.get('src'),
        }

        i += 1

        filename = str(i) + '.'+data['title'][0] + " " + data['rate'][0] + '分.jpg'
        pic = requests.get(data['image_url'])
        with open('/Users/sandisk/Desktop/Spider_douban/doouban_top250/'+filename , 'wb') as f:
            f.write(pic.content)
        print(data)

