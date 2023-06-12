#!/bin/bash

# Infinite loop
while true; do
    # Ping to google.com every 5s until it reaches 60s
    # then, select only the min, avg, max ping times in ms
    ping_info=$(ping -i 5 -w 60 google.com | tail -1 | sed 's/.* = \(.*\)\/.* ms/\1/' | tr / ,)

    # Gather time and date information
    current_date=$(date +"%Y-%m-%d")
    current_time=$(date +"%H:%M:%S")

    echo "$ping_info,$current_time,$current_date" > ping.csv
done

