import sys
import re

from Concept import *

if len(sys.argv) == 1:
    print("No files provided.")
    exit()

ConceptList = [Concept("Conditionals"), Concept("Loop"), Concept("Display")]

for filename in sys.argv[1:]:
    relations = set()
    f = open(filename, 'r')
    text = f.read()

    for concept in ConceptList:
        for regex in concept.regex:
            if re.search(regex, text):
                relations.add(concept.name)

    print("File " + filename + " has relations:")
    print(relations)
