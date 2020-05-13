import requests
import json


def recomand(word):
    baseurl = "https://tastedive.com/api/similar"
    params_d = {"q": word, "type": "movies", "limit": "5"}

    resp = requests.get(baseurl, params=params_d)
    # print(type(resp))
    # print(resp.url)
    # print(resp.text)
    word_ds = resp.json()
    # print(type(word_ds))
    # print(word_ds)
    new_d = (word_ds['Similar']['Results'])
    return [d['Name'] for d in new_d]


print("Enter movie Name : ")
word = input()
print(recomand(word))
