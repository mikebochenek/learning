#!/bin/sh

# since you cannot trust anyone or anything these days, the below script
# will clone all my github projects into a tmp directory and zip them up for shipping

cd /tmp
MYNOW=$(date +"%F-%H.%M.%S")
mkdir backup-$MYNOW
cd backup-$MYNOW
git clone https://github.com/mikebochenek/learning
