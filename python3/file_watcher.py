# based on https://stackoverflow.com/questions/33571641/a-python-script-to-monitor-a-directory-for-new-files

from time import sleep
import os
from datetime import datetime
import requests

'''
? maybe can be combined with "new" photos from: 
https://www.ezone.co.uk/blog/using-developer-tools-to-transfer-files-on-android.html
*** 'find and pull movies out of camera storage' ***
adb shell 'find /storage/emulated/0/DCIM/Camera/ -name "*.mp4" -print0' | xargs -0 -n 1 adb pull
? and where do I get the OCR again? from the view controller? 

~/Android/Sdk/platform-tools/adb shell 'find /storage/self/primary/DCIM/Camera/ -name "IMG_20240818*.jpg" -print0' | xargs -0 -n 1 ~/Android/Sdk/platform-tools/adb pull
'''

cmd1 = "~/Android/Sdk/platform-tools/adb shell 'find /storage/self/primary/DCIM/Camera/ -name \"IMG_"
# IMG_20240818*.jpg
cmd_filemask = "20240818" # IMG_20240818_174542_865 or IMG_20240818_174555_341 
cmd2 = "*.jpg\" -print0' | xargs -0 -n 1 ~/Android/Sdk/platform-tools/adb pull"

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
    d = now.strftime('%Y%m%d_%H%M') #'2024-08-21 19:27:01.859555'
    # print(now, '--->', d)

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