"""
API to generate word counts and get word count
"""

import json
from collections import Counter
import codecs

from bottle import route, run, request

import logging
logging.basicConfig(filename='API.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

# Generate word counts from big.txt
word_counts = dict(Counter(codecs.open('big.txt', 'rb', 'utf-8').read().strip().lower().split()))

# TODO:
"""
1. Write a function to preprocess+clean data from "big.txt" - DONE
2. Generate a collections Counter object - DONE
3. Load the counter object in memory before starting the API - DONE
4. Get the API to provide Top N (configurable) words (MAKE SURE TO ACCOUNT FOR ERRORS !!) - DONE
5. Get the word count for a word - DONE
6. Update the count of a word in the dictionary - DONE
7. Delete a word from the counter object - DONE
8. Bundle the API in a Docker image
9. Deploy the Docker API on the cloud
10.Push the docker image to DockerHub

"""

@route('/words/')
def list_word_counts():
    """
    Get the complete list of words with their word counts
    :return: dict, return status and dicts with key (word) and value (word count)
    """
    return {"success": True, "info": word_counts}


@route('/words/top/<n:int>', method='GET')
def list_top_word(n):
    """
    get the top N words from the word count dictionary
    :param n: int, Number of words to return from the dictionary
    :return: dict, return status and dicts with key (word) and value (word count) of Top N words
    """
    return {"success": True, "info": dict(word_counts.items()[:n])}


@route('/words/counts/<word>', method='GET')
def get_word_count(word):
    """
    Get the count of a word in the word count dictionary
    :param word: str, word for which a word count must be returned
    :return: dict, return success status and count of the word provided by the user
    """
    try:
        return {"success": True, "count": word_counts[word]}
    except KeyError:
        return {"success": False, "info": "Word < %s > doesn't exist in the dictionary"%word}

@route('/words/add', method='PUT')
def add_word():
    """
    Add/Update a word count in the word count dictionary
    :return: dict, return success status and information of the word added in the dictionary
    """
    data = json.loads(request.body.read())
    word_counts.update(data)
    return {"success": True, "info": "Word < %s > added in the dictionary!" % data.keys()[0]}


@route('/words/remove/<word>', method='DELETE')
def remove_word(word):
    """
    Remove a word count in the word count dictionary
    :param word: str, word which must be removed from the dictonary
    :return: dict, return success status and information of the word deleted from the dictionary
    """
    word_counts.pop(word)
    return {"success": True, "info": "Word < %s > removed from the dictionary!" % word}


if __name__ == '__main__':
    run(host='0.0.0.0', port=8088, debug=True)
