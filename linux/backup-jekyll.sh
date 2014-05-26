#!/bin/sh

cd ~/Dev/learning/blog
jekyll build
cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-jekyllsite-$MYNOW

cd backup-jekyllsite-$MYNOW

cp -r cd ~/Dev/learning/blog/_site/ .
cd /tmp
tar cvf backup-jekyllsite-$MYNOW.tar /tmp/backup-jekyllsite-$MYNOW/*
gzip backup-jekyllsite-$MYNOW.tar
cp backup*.gz ~/Dropbox/backups/

