#!/bin/bash

DIRECTORY=$(cd `dirname $0` && pwd)
cd $DIRECTORY/sentinelfrontend
source $DIRECTORY/venv/bin/activate
$DIRECTORY/venv/bin/python3 $DIRECTORY/run.py & 

sleep 5
$DIRECTORY/venv/bin/python3 $DIRECTORY/sentinelfrontend/main.py

