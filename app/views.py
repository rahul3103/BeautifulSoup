from flask import render_template
from bs4 import BeautifulSoup, element
import urllib2
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Rahul'}
	i=1
	count =1
	items = []
	heads = []
	bodys = []
	writers = []
	dates=[]
	m = 0
	while(i<21):
		url = 'http://www.goal.com/en-gb/rumours/last/168?page='+str(i)+'&ICID=OP'
		response = urllib2.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html)
		i +=1

		# Collect rumors posts
		rumour_post_tags = soup.find_all("div", {"id":"rumours"})

		
		for rumour_tags in rumour_post_tags:
			content_tags = rumour_tags.find_all("div",{"class":"rumour-content"})
			for rumour in content_tags:
				items.append(count)
				count +=1
				heads.append(rumour.find("h3",{'class':'column'}).text)
				bodys.append(rumour.find('p').text)
				for sources in rumour.find_all('span',{'class':'column'}):
  					for source in sources:
  						if m %2 == 0:
  							writers.append(source)
  							m += 1
  						else:
  							dates.append(source)
  							m +=1

  	
	return render_template('index.html',allitems=zip(items,heads,bodys,writers,dates))