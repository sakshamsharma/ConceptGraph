import sys
import re
import subprocess

from Concept import *

if len(sys.argv) == 1:
    print("No files provided.")
    exit()

if sys.version_info >= (3, 0):
    conceptsInDir = subprocess.getoutput('ls data').split('\n')
else:
    conceptsInDir = subprocess.check_output(['ls', 'data']).split('\n')[:-1]

ConceptList = []
for concept in conceptsInDir:
    ConceptList.append(Concept(concept))

for filename in sys.argv[1:]:
    relations = set()
    f = open(filename, 'r')
    text = f.read()

    for concept in ConceptList:
        isUnmatched = 0
        for unmatcher in concept.unmatchers:
            if re.search(unmatcher, text):
                isUnmatched = 1
                break
        if isUnmatched:
            continue
        for regex in concept.regex:
            if re.search(regex, text):
                relations.add(concept.name)

    print("File " + filename + " has relations:")
    print(list(relations))
