#!/bin/bash


echo "venv actication"
source ./src/bin/activate
echo "venv activation successful"

echo "port initialization"
sudo chmod a+rwx $1
echo "port initialization successful"

echo "script launching"
sudo python3 ./src/main.py
echo "end of the debug session"
