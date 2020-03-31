import requests
import sys
import json


def get_links(query):
    links = []
    s = requests.Session()
    print(s)
    search = query
    apiKey='AIzaSyBwztasUrFiro_qsE8pD-maCL_m8JrgMcQ'
    cx='013994057420626416686:kihsqrvoppq'
    body = s.get(f'https://www.googleapis.com/customsearch/v1?q={search}&key={apiKey}&cx={cx}&num=10&searchtype=image', params = {})
    #print(body.content)
    data=json.loads(body.content)
    return data
    # for img in data["items"]:
    #     links.append(img["pagemap"]["cse_image"][0]["src"]) 
    # return links