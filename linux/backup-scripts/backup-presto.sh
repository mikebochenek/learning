#!/bin/sh

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-presto-$MYNOW
cd backup-presto-$MYNOW

cp -r /home/mike/Documents/prestop/ .

cd /tmp
tar cvf backup-presto-$MYNOW.tar /tmp/backup-presto-$MYNOW/*
gzip backup-presto-$MYNOW.tar
cp backup-presto*.gz ~/Dropbox/backups/
cp backup-presto*.gz ~/Dropbox/presto_private/backup/backend-code/


