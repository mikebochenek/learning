#!/bin/sh

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-idoneweb-$MYNOW
cd backup-idoneweb-$MYNOW

# old HP laptop
# cp -r /home/mike/Dev/AptanaWorkspace/idone-bootstrap/ .
# cp -r /home/mike/Dev/AptanaWorkspace/idone-coming/ .
# cp -r /home/mike/Dev/AptanaWorkspace/bochenek-ch/ .
# cp -r /home/mike/Dev/AptanaWorkspace/fitness/ .
# cp -r /home/mike/Dev/AptanaWorkspace/play/ .
# cp -r /home/mike/Dev/AptanaWorkspace/maps/ .

# new HP laptop
cp -r /home/mike/Documents/static-html/idone-bootstrap/ .
cp -r /home/mike/Documents/static-html/idone-coming/ .
cp -r /home/mike/Documents/static-html/bochenek-ch/ .
cp -r /home/mike/Documents/static-html/fitness/ .
cp -r /home/mike/Documents/static-html/play/ .
cp -r /home/mike/Documents/static-html/maps/ .

cd /tmp
tar cvf backup-NEW-idoneweb-$MYNOW.tar /tmp/backup-idoneweb-$MYNOW/*
gzip backup-NEW-idoneweb-$MYNOW.tar
cp backup*.gz ~/Dropbox/backups/
