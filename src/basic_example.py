import filequery as fq

results = fq.findall("react-native", extensions=[".md"], folders=["../"])

print(results.head())