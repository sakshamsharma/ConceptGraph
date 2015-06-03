import re

class Concept:
    def __init__(self, name):
        self.name = name
        self.regex = []
        f = open('data/'+name, 'r')
        self.populateRegex(f)
        f.close()

    def populateRegex(self, f):
        for line in f:
            isSimple = re.search('\\ ', line)
            if not isSimple:
                self.regex.append(line.rstrip('\n'))
