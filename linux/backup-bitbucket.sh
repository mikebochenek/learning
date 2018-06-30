#!/bin/sh

# since you cannot trust anyone or anything these days, the below script
# will clone all my bitbucket projects into a tmp directory and zip them up for shipping
# similar to my backup-github.sh script

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-$MYNOW
cd backup-$MYNOW

# my repos
git clone https://bitbucket.org/futration/spark-intercooler
git clone https://bitbucket.org/mikey320b/jupyter-notebooks
git clone https://bitbucket.org/futration/yakondiandroid
git clone https://bitbucket.org/mikey320b/voicebot
git clone https://bitbucket.org/mikey320b/reactbites
git clone https://bitbucket.org/mikey320b/redux
git clone https://bitbucket.org/bitesapp/bitesandroidrepo
git clone https://bitbucket.org/mikey320b/prestop
git clone https://bitbucket.org/bitesapp/bitesrepo
git clone https://bitbucket.org/futration/firebase
git clone https://bitbucket.org/futration/rtc
git clone https://bitbucket.org/mikey320b/spark-presto

cd /tmp
tar cvf backup-$MYNOW.tar /tmp/backup-$MYNOW/*
gzip backup-$MYNOW.tar
# cp backup*.gz ~/Dropbox/backups/
cp backup*.gz ~/Documents/backups/
