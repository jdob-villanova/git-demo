#! /usr/bin/python

import random

# read all the names
file = open('names/first-names.txt')
firstNames = file.readlines()
file.close

# read all the places
file = open('names/places.txt')
places = file.readlines()
file.close

for x in range( 0, 10 ):
  # randomize the arrays
  random.shuffle(firstNames)
  random.shuffle(places)

  # show where they visited, but each first name will be removed
  # after being printed, ensuring it only shows once
  print "%s visted %s!" % (firstNames.pop().rstrip(), places[0].rstrip())

