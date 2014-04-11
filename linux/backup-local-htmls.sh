#!/bin/sh

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-idoneweb-$MYNOW
cd backup-idoneweb-$MYNOW

cp -r /home/mike/Dev/AptanaWorkspace/idone-bootstrap/ .
cp -r /home/mike/Dev/AptanaWorkspace/idone-coming/ .
cp -r /home/mike/Dev/AptanaWorkspace/bochenek-ch/ .
cp -r /home/mike/Dev/AptanaWorkspace/fitness/ .
cp -r /home/mike/Dev/AptanaWorkspace/play/ .

cd /tmp
tar cvf backup-idoneweb-$MYNOW.tar /tmp/backup-idoneweb-$MYNOW/*
gzip backup-idoneweb-$MYNOW.tar
cp backup*.gz ~/Dropbox/backups/
