import json
import requests

def testloop():
    for i in range(126005, 21124826):

        response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty')
        getjson = response.json()
        #use this to open
        if getjson is None:
            print([i])
            print('missing title')
            pass

        elif 'title' in getjson:
            gettitle = response.json()['title']
            f = open("Hackednews.txt", "a", encoding="utf-8")
            f.write(gettitle + "\r\n" + "<|endoftext|>\r\n")
            f.close
            print([i])
            print(response.json()['title'])

        else:
            pass


testloop()
