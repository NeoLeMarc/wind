#!/bin/bash
while 1;
do
    cd ~/Wind
    python -OO new_wind.py
    echo "Ended unexpectedly... restarting in 10 seconds"
done
