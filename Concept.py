import re

class Concept:
    def __init__(self, name):
        self.name = name
        self.regex = []
        self.unmatchers = []
        f = open('data/'+name, 'r')
        self.populateRegex(f)
        f.close()

    def populateRegex(self, f):
        for line in f:
            if line == "\n" or line == "":
                continue
            if line[0] == "!":
                unmatch = 1
                line = line[1:]
            else:
                unmatch = 0
            hasSpaces = re.search('\\ ', line)
            if not hasSpaces:
                if unmatch:
                    self.unmatchers.append(line.rstrip('\n'))
                else:
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
                        if word[0] == '.':
                            reg += '(\w+\s){0,%s}' % len(word)
                        else:
                            reg += '(\w+\s){%s,%s}' % (len(word), len(word))
                if unmatch:
                    self.unmatchers.append(reg)
                else:
                    self.regex.append(reg)
