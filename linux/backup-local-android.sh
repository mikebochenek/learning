#!/bin/sh

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-android-$MYNOW
cd backup-android-$MYNOW

# old HP laptop
# cp -r /home/mike/Dev/adt-workspace4/fitness/ .
# cp -r /home/mike/Dev/adt-workspace4/TouchMemoryCH/ .

# new HP laptop
cp -r /home/mike/AndroidstudioProjects/TouchMemoryCH/ .

cd /tmp
tar cvf backup-NEW-android-$MYNOW.tar /tmp/backup-android-$MYNOW/*
gzip backup-NEW-android-$MYNOW.tar
cp backup*.gz ~/Dropbox/backups/
mv /tmp/backup-NEW-android-$MYNOW.tar.gz /tmp/current-version-android.tar.gz
# mv /tmp/current-version-android.tar.gz ~/Dropbox/fitness_app/
