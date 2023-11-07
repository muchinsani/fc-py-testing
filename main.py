import json
import requests

def handler(environ, start_response):
    r = requests.get('https://github.com/timeline.json')
    # return r.json()
    # return '{ "name":"John", "age":30, "city":"New York"}'
    print(r.content)
    return r.content
