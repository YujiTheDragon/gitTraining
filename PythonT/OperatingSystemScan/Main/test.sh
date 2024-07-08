#!/bin/bash

file_path="C:/Users/KAY3SF/Desktop/Training/PythonT/OperatingSystemScan/Main/PC_LOGS.txt"


py main.py
if [ ! -s "$file_path" ]; then

echo "ERROR"
cat PC_LOGS.txt
exit 1

fi

cat PC_LOGS.txt
echo "Successfully ran PC scan"