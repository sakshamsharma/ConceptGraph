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
            hasSpaces = re.search('\\ ', line)
            if not hasSpaces:
                self.regex.append(line.rstrip('\n'))
            else:
                reg = r"\b"
                # Creating a matching pattern
                # For example this:
                # p = re.compile(r'\bfor\s(\w+\s){2,2}while\b')
                # This matches "for <2 words> while"
                words = line.rstrip('\n').split(' ')
                for i in range(0, len(words)):
                    word = words[i]
                    if i%2 == 0:
                        reg += '{0}\s'.format(word)
                    else:
                        reg += '(\w+\s){1,%s}' % len(word)
                self.regex.append(reg)
