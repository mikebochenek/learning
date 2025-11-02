#!/bin/sh

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-android-$MYNOW
cd backup-android-$MYNOW

cp -r /home/mike/Dev/adt-workspace4/fitness/ .

cd /tmp
tar cvf backup-android-$MYNOW.tar /tmp/backup-android-$MYNOW/*
gzip backup-android-$MYNOW.tar
cp backup*.gz ~/Dropbox/backups/
mv /tmp/backup-android-$MYNOW.tar.gz /tmp/current-version-android.tar.gz
mv /tmp/current-version-android.tar.gz ~/Dropbox/fitness_app/
