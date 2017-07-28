import requests
from requests.auth import HTTPBasicAuth

url='http://moniter.nc.jogos321.com.br/narutogames/index.php?model=user_new_outline&addition=user_new_outline&agentid=102&amp;sort=id&amp;order=asc'
r=requests.get(url,auth = HTTPBasicAuth('wanghaoran','VQH*2zAcKe'))

