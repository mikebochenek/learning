# based on https://stackoverflow.com/questions/33571641/a-python-script-to-monitor-a-directory-for-new-files

from time import sleep
import os
import sys
from datetime import datetime
import requests

from try_vertexai import generate
from ocr import detect_text

sep = '\n---------------\n'
path_to_watch = sys.argv[1] # "/home/mike/Pictures"
print(datetime.now(), '*starting to watch path: "',path_to_watch,'"')

before = dict ([(f, None) for f in os.listdir (path_to_watch)])

while 1:
    sleep(0.1)
    now = datetime.now()
    d = now.strftime('%Y%m%d_%H%M') #'2024-08-21 19:27:01.859555'
    # print(now, '--->', d)

    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    if added:
        print('  ', now, "Added: ", ", ".join (added))
        # print (added)  # is an array of strings - i.e. ['Screenshot from 2024-02-18 22-05-59.png']
        for a in added:
            dt = detect_text(path_to_watch + '/' + a)
            print (dt, sep)            
            a = generate(dt)
            print (a, sep)
        before = after
        #break
    else:
        before = after
        #print(now, "no change", len(before))


# print (detect_text('/home/mike/Downloads/20240202_153004.jpg'))

'''
generate(
    """Read the below multiple choice question carefully, and provide the best answer:

  Git. You first sum 2 and two, and then multiply the result by four. What is the outcome of this operation?
  (a) 16
  (b) 10
  (c) sixteen
  (d) A failure because you cannot add before multiplication""")
'''
