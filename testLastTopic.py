from platforms.xenforo import Xenforo
import requests


base_url = 'http://www.webcheats.com.br'

xenforo  = Xenforo(base_url)

if xenforo.login('', ''):

 url_posts = '{}/find-new/posts'.format(base_url) 

 r = requests.get(base_url)
 html = str(r.content)
 initial = 15

 lastId = html[int(html.find('<li id="thread-'))+initial]


 while(lastId.isdigit()):
  lastId += html[int(html.find('<li id="thread-'))+initial]
  initial+= 1

 lastId = lastId.replace('"', '')
 print ('Ultimo Topico: ' + lastId)
