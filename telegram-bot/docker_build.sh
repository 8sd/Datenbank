#/bin/sh

cp ../list ./list
#check for $1 if is set and use as Tag
docker build . -t datenbankbot:latest
rm ./list
