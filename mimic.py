#!/usr/bin/python -tt
# based on 
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class
"""

import random
import sys

def mimic_dict(text):
  """Returns mimic dict mapping each word to list of words which follow it."""
  mimic_dict = {}
  words = text.split()
  prev = ''
  for word in words:
    if not prev in mimic_dict:
      mimic_dict[prev] = [word]
    else:
      mimic_dict[prev].append(word)
    prev = word
  return mimic_dict


def mimic(text, word=''):
  """Given mimic dict and start word, prints 200 random words."""
  mdict = mimic_dict(text)
  ret = []
  for unused_i in range(24):
    ret.append(word),
    nexts = mdict.get(word)
    if not nexts:
      nexts = mdict['']
    word = random.choice(nexts)
  return ' '.join(ret)
