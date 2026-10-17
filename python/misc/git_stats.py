# https://www.feststelltaste.de/reading-a-git-repos-commit-history-with-pandas-efficiently/
# https://gitpython.readthedocs.io/en/stable/tutorial.html#using-git-directly
import git 

#GIT_REPO_PATH = r'/home/mike/code/learning/'
GIT_REPO_PATH = r'/home/mike/code/spark-intercooler/'
#GIT_REPO_PATH = r'/home/mike/code/yakondi2/'
repo = git.Repo(GIT_REPO_PATH)
git_bin = repo.git
print (git_bin)

master = repo.heads.master
print (len(master.log()))

git_log = git_bin.execute('git log --numstat --pretty=format:"\t\t\t%h\t%at\t%aN"', shell=True)
print (len(git_log))

import pandas as pd
from io import StringIO

commits_raw = pd.read_csv(StringIO(git_log), 
    sep="\t",
    header=None,              
    names=['additions', 'deletions', 'filename', 'sha', 'timestamp', 'author']
    )
print(commits_raw.head())
print(commits_raw.info())
print(commits_raw.groupby(['author']).size())


'''
- all in vain... 
import os
os.environ['GIT_PYTHON_GIT_EXECUTABLE'] = '/usr/bin/'
print(os.getenv('GIT_PYTHON_GIT_EXECUTABLE'))
print(os.getenv('PATH'))

#git_log = git_bin.execute('git log --numstat --pretty=format:"\t\t\t%h\t%at\t%aN"')
git_log = git_bin.execute('git log --numstat')
print (git_log[:3])
'''