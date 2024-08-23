# based on https://stackoverflow.com/questions/33571641/a-python-script-to-monitor-a-directory-for-new-files

from time import sleep
import os
from datetime import datetime
import subprocess # https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output

'''
https://www.ezone.co.uk/blog/using-developer-tools-to-transfer-files-on-android.html
*** 'find and pull movies out of camera storage' ***
adb shell 'find /storage/emulated/0/DCIM/Camera/ -name "*.mp4" -print0' | xargs -0 -n 1 adb pull
~/Android/Sdk/platform-tools/adb shell 'find /storage/self/primary/DCIM/Camera/ -name "IMG_20240818*.jpg" -print0' | xargs -0 -n 1 ~/Android/Sdk/platform-tools/adb pull
'''

cmd1 = "~/Android/Sdk/platform-tools/adb shell 'find /storage/self/primary/DCIM/Camera/ -name \"IMG_"
# IMG_20240818*.jpg
cmd_filemask = "20240818" # IMG_20240818_174542_865 or IMG_20240818_174555_341 
cmd2 = "*.jpg\" -print0' | xargs -0 -n 1 ~/Android/Sdk/platform-tools/adb pull"

print(datetime.now(), '*starting to slurp..')

while 1:
    sleep(0.5) # wait after trying to copy, which is good enough..?
    now = datetime.now()
    d = now.strftime('%Y%m%d_%H%M') #'2024-08-21 19:27:01.859555'
    #print(now, os.getcwd(), '--->', d)
    mycmd = cmd1 + d + cmd2
    #print(mycmd)
    output = subprocess.getoutput(mycmd)
    if "pull requires an argument" not in output and 'no devices' not in output:
        print(output)
    else:
        pass #print('nothing found...')
    
