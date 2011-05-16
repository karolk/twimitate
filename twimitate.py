#!/usr/bin/python -tt

import twittersearch
import mimic

def sample(username):
    ts = twittersearch.Twitter()
    tweets = ts.search('from:'+username)
    sample = ''
    for tweet in tweets:
      sample += tweet[u'text']
    return sample
    
def imitate(username):
    return mimic.mimic(sample(username))