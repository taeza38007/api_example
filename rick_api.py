#!/usr/local/bin/python3
import requests
import json
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

# Fuction to fetch json data from 'baseurl' & 'endpoint'
def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?pages={x}')
    return r.json()

# Get number of pages in 'data'(response)
def get_pages(response):
    return(response['info']['pages'])

# Fuction that loop through all item in 'data' 
def parse_json(response):
    character_list = []
    for item in response['results']:
        # print(item['name'], len(item['episode']))
        char = {
            'id': item['id'],
            'name': item['name'],
            'number_ep': len(item['episode'])
        }
        character_list.append(char)
    return character_list

    # name = response['results']
    # episodes = response['episodes']

data = main_request(baseurl, endpoint, 1)
pages = get_pages(data)
name = data['results'][0]['name']
episodes = data['results'][0]['episode']

# print(episodes)
# print(len(episodes))
# print(name)
# print(pages)

# parse_json(data)
print(parse_json(data))

mainlist = []
for i in range(1, get_pages(data) + 1):
    print(i)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, i)))

print(len(mainlist))

# print(pages)
df = pd.DataFrame(mainlist)
print(df.head(), df.tail())

df.to_csv('character_list.csv', index=False)

