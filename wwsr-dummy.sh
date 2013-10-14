#!/bin/bash
#echo -e "N `shuf -i 0-360 -n 1` 0.0"
SPEED=`shuf -i 0-200 -n 1`
SPEED=`echo "scale=1; $SPEED/10" | bc`
#echo -e "N 0 0.0"
echo -e "N 0 $SPEED"
