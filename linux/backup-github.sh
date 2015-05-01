#!/bin/sh

# since you cannot trust anyone or anything these days, the below script
# will clone all my github projects into a tmp directory and zip them up for shipping

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-$MYNOW
cd backup-$MYNOW

# my repos
git clone https://github.com/mikebochenek/angular-jboss-blog
git clone https://github.com/mikebochenek/html5
git clone https://github.com/mikebochenek/learning
git clone https://github.com/mikebochenek/brainstorm
git clone https://github.com/mikebochenek/zoo-mint
git clone https://github.com/mikebochenek/adt-workspace
git clone https://github.com/mikebochenek/adt-workspace3
git clone https://github.com/mikebochenek/adt-workspace4
git clone https://github.com/mikebochenek/myapp0
git clone https://github.com/mikebochenek/zoo
git clone https://github.com/mikebochenek/vantaa
git clone https://github.com/mikebochenek/mychat
git clone https://github.com/mikebochenek/college
git clone https://github.com/mikebochenek/cvparse
git clone https://github.com/mikebochenek/idone
git clone https://github.com/mikebochenek/eventual
git clone https://github.com/mikebochenek/idonep
git clone https://github.com/mikebochenek/swiss-memory

# other repos
git clone https://github.com/jjenkov/scale

cd /tmp
tar cvf backup-$MYNOW.tar /tmp/backup-$MYNOW/*
gzip backup-$MYNOW.tar
cp backup*.gz ~/Dropbox/backups/
