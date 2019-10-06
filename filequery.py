import glob
import re

def file_query(folder, query, extensions=[], recursive=True):

    for ext in extensions:

        files = glob.glob(f"{folder}\**\*{ext}", recursive=recursive)
        matches = []

        for file in files:
            f = open(file, "r")
            content = f.read()

            if (callable(query)):
                matches.extend(query(content))
            else:
                matches = re.finditer(query, content, re.MULTILINE)
                for matchNum, match in enumerate(matches, start=1):
                    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            f.close()


file_query('.','file_query', extensions=['.py'])