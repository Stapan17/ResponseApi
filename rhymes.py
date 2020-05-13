import requests
import json

# # import statements for necessary Python modules
# import requests


# def get_rhymes(word):
#     baseurl = "https://api.datamuse.com/words"
#     params_diction = {}  # Set up an empty dictionary for query parameters
#     params_diction["rel_rhy"] = word
#     params_diction["max"] = "3"  # get at most 3 results
#     resp = requests.get(baseurl, params=params_diction)
#     # return the top three words
#     word_ds = resp.json()
#     return [d['word'] for d in word_ds]
#     return resp.json()  # Return a python object (a list of dictionaries in this case)


# print(get_rhymes("sad"))


def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_d = {"rel_rhy": word, "max": "5"}

    resp = requests.get(baseurl, params=params_d)
    # print(resp.text)
    # print(resp.url)
    word_ds = resp.json()
    # print(type(word_ds))
    # print(word_ds)
    return [d['word'] for d in word_ds]


print("Enter Anything You Want: ")
word = input()
print(get_rhymes(word))
