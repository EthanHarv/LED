#!/bin/bash
sleep 5
screen -d -m -S serv bash -c 'cd /home/pi/LED && sudo python3 DynamicLEDServer.py'
