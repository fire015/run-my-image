#!/usr/bin/env bash
set -e

i=0

echo "[$(date +%Y-%m-%d-%H:%M:%S)] Starting now..."

while [ $i -le 10 ]
do
    curl -sS "http://worldtimeapi.org/api/ip" > /dev/stdout
    echo ""
    sleep 5
    i=$(( $i + 1 ))
done

echo "[$(date +%Y-%m-%d-%H:%M:%S)] Goodbye..."