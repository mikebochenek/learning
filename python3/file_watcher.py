# based on https://stackoverflow.com/questions/33571641/a-python-script-to-monitor-a-directory-for-new-files

from time import sleep
import os
from datetime import datetime
import requests

path_to_watch = "/home/mike/Pictures"
print(datetime.now(), '*starting to watch path: "',path_to_watch,'"')

before = dict ([(f, None) for f in os.listdir (path_to_watch)])

# https://stackoverflow.com/questions/2486145/python-check-if-url-to-jpg-exists
def urlexists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

print (urlexists('https://bochenek.ch/tmp/aoc2023/ocr/Screenshot%20from%202024-02-18%2022-38-47.png'))

while 1:
    sleep(0.1)
    now = datetime.now()

    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    if added:
        print(now, "Added: ", ", ".join (added))
        # print (added)  # is an array of strings - i.e. ['Screenshot from 2024-02-18 22-05-59.png']
        before = after
        #break
    else:
        before = after
        #print(now, "no change", len(before))