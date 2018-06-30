"""
API to generate word counts and get word count
"""

import json
import os
from bottle import route, run, request

# TODO: Replace this with a collections Counter object
word_counts = {'word': 10, 'is': 123, 'good': 5}

# TODO:
"""
1. Write a function to preprocess+clean data from "big.txt" 
2. Generate a collections Counter object
3. Load the counter object in memory before starting the API
4. Get the API to provide Top N (configurable) words (MAKE SURE TO ACCOUNT FOR ERRORS !!)
5. Get the word count for a word
6. Update the count of a word in the dictionary
7. Delete a word from the counter object
8. Bundle the API in a Docker image
9. Deploy the Docker API on the cloud
10.Push the docker image to DockerHub

"""


# TODO: Add logging in each function and save to a logfile

@route('/words/')
def list_word_counts():
    return {"success": True, "info": word_counts}


@route('/words/top/<n:int>', method='GET')
def list_top_word(n):
    return {"success": True, "info": dict(word_counts.items()[:n])}


@route('/words/counts/<word>', method='GET')
def get_word_count(word):
    # TODO: Return error statements
    return {"success": True, "count": word_counts[word]}


@route('/words/add', method='PUT')
def add_word():
    # TODO: Account for adding multiple words
    data = json.loads(request.body.read())
    word_counts.update(data)
    return {"success": True, "info": "Word %s added in the dictionary!" % data.keys()[0]}


@route('/words/remove/<word>', method='DELETE')
def remove_word(word):
    return {"success": True, "info": "Word %s removed from the dictionary!" % word}


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
