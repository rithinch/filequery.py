import glob
import re
import os
import pandas as pd

def _get_matches_data(pattern, string, filename):
    '''
    A version of 're.finditer' that returns '(match, line_number)' pairs.
    '''
    f = os.path.basename(filename)
    directory_name = os.path.dirname(filename)

    matches = list(re.finditer(pattern, string, re.MULTILINE))

    if not matches:
        return []

    end = matches[-1].start()
    # -1 so a failed 'rfind' maps to the first line.
    newline_table = {-1: 0}
    for i, m in enumerate(re.finditer(r'\n', string), 1):
        # don't find newlines past our last match
        offset = m.start()
        if offset > end:
            break
        newline_table[offset] = i

    # Failing to find the newline is OK, -1 maps to 0.
    results = []

    for m in matches:
        newline_offset = string.rfind('\n', 0, m.start())
        newline_end = string.find('\n', m.end())  # '-1' gracefully uses the end.
        line = string[newline_offset + 1:newline_end]
        line_number = newline_table[newline_offset]
        
        results.append((f, directory_name, line_number, m.group(), line))
    
    return results

def findall(query, extensions=[], folders=[], recursive=True):
    
    results = []

    for folder in folders:

        for ext in extensions:

            #Fix to support both mac and windows - forward/backward slashes and unix
            path = os.path.join(folder,"**",f"*{ext}")
            print(path)
            files = glob.glob(path, recursive=recursive)

            for file in files:

                results.extend(find(query, file, to_df=False))

    return pd.DataFrame(results, columns=['Filename', 'Folder Path', 'Line Number', 'Match', 'Full Line'])

def find(query, file, to_df=True):

    results = []

    try:
        f = open(file, "r")
        content = f.read()
    except UnicodeDecodeError as e:
        f = open(file, "r", encoding='cp1252')
        content = f.read()
    except PermissionError as e:
        return results

    if (callable(query)):

        return query(content)

    else:

        results = _get_matches_data(query, content, file)

    f.close()

    if to_df:
        return pd.DataFrame(results, columns=['Filename', 'Folder Path', 'Line Number', 'Match', 'Full Line'])

    return results
