import filequery as fq

results = fq.findall("content", extensions=[".md"], folders=["../"])

print(results.head())