import glob
import re

def findall(query, extensions=[], folders=[], recursive=True):
    
    matches = []

    for folder in folders:
        for ext in extensions:
            files = glob.glob(f"{folder}\**\*{ext}", recursive=recursive)
            for file in files:
                matches.extend(find(query, file))

def find(query, file):
    f = open(file, "r")
    content = f.read()

    if (callable(query)):
        return query(content)
    else:
        matches = re.finditer(query, content, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    f.close()

def save(results, name, location):
    pass

findall('file_query', extensions=['.py'], folders=['*'])