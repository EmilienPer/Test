#!/bin/bash

while true
do
    for i in {1..$(( $RANDOM % 10+ 1 ))}; do
        curl --silent "https://devops-talk.herokuapp.com/" -o /dev/null
        echo $i
    done
    sleep 5s
done
