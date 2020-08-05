# :mag_right: filequery.py
Search for content in your local files and get results in a friendly format. 

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rithinch_filequery.py&metric=alert_status)](https://sonarcloud.io/dashboard?id=rithinch_filequery.py)

### Motivation

### Uses

- Get matches as a pandas dataframe - can conduct further analysis on file content directly in jupyter notebook
- Find and report content matches in a format of your choice (csv, excel, json, sql)
- Hackable/Flexible

### Roadmap
- Add support mac/linux file systems in findal all method when getting globs
- Results merge
- Excluding certain filenames, or foldernames. - Exclusions list
- Pass custom query function return i.e. list of tuples, with flexible column names.
- Ability to find and replace regex matching strings with custom functions.
- Regex groups support - when returning to csv.
- Make this pip installable package - With Github open source project style.
- Add an suitable project name.
- Pandas DF lets you save to save to csv, excel, json etc. with all df functionality.
- CLI - call directly from command line. 

