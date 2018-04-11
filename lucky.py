#!python3

import requests,bs4,webbrowser,sys

URL='https://www.baidu.com/s?wd=' + ''.join(sys.argv[1:])
headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36"
}


print('Googling...')
res=requests.get(URL,headers=headers)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,'html.parser')
linkElems=soup.select('.t a')

numOpen=min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open(linkElems[i].get('href'))


