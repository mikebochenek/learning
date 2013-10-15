#!/bin/sh

cd ~/Dev/workspace/zoo-mint
MYNOW=$(date +"%F-%H.%M.%S")
mvn clean test >> /tmp/$MYNOW.log
tail /tmp/$MYNOW.log >> ~/Dev/learning/selenium/logs/auto-append.log
cd ~/Dev/learning/selenium/logs/
git commit auto-append.log -m 'automagically adding selenium tests output to master log'
git push
echo '.... all done ....'
tail /tmp/$MYNOW.log
