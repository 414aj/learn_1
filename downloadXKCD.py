#!python3

import requests,bs4,os

URL='https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not URL.endswith('#'):
	print('Downloading page %s...' % URL)
	res=requests.get(URL)
	res.raise_for_status()

	soup=bs4.BeautifulSoup(res.text) 
	comicElem=soup.select('#comic img')
	if comicElem==[]:
		print('Could not find comic image')
	else:
		comicURL='http:'+comicElem[0].get('src')
		print('Downloading image %s...' % (comicURL))
		res=requests.get(comicURL)
		res.raise_for_status()

	imageFile=open(os.path.join('xkcd',os.path.basename(comicURL)),'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	prevURL=soup.select('a[rel="prev"]')[0]
	URL='https://xkcd.com'+prevURL.get('href')

print('Done')