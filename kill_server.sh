#!/bin/bash

PID=$(pgrep -of runserver)

echo "process id of server:"$PID

kill $PID

echo "the server has stopped"
