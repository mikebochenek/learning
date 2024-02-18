# based on https://stackoverflow.com/questions/33571641/a-python-script-to-monitor-a-directory-for-new-files

from time import sleep
import os
from datetime import datetime

path_to_watch = "/home/mike/Pictures"
print(datetime.now(), '*starting to watch path: "',path_to_watch,'"')

before = dict ([(f, None) for f in os.listdir (path_to_watch)])

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