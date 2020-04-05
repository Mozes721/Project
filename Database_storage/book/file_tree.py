import os, re
import os.path as path

def find_files(pattern, base='.'):

    regex = re.compile(pattern)
    matches = []

    for root, dir, file in os.walk(base):
        for f in file:
            if regex.matches(f):
                matches.append(os.path.join(root, f))
    return matches

