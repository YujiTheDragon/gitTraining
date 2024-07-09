#!/bin/bash

dir_path=~/Desktop/PC_SCAN
PYTHON_EXE=py
if ! command -v py &>/dev/null; then
    echo "PY not found using PYTHON"
    PYTHON_EXE=python
fi

if [ -d "$dir_path" ]; then
    cd ~/Desktop/PC_SCAN/gitTraining/PythonT/OperatingSystemScan
    $PYTHON_EXE main.py
    cat PC_LOGS.txt
    echo "Successfully ran PC scan"
else
    echo "Files not found installing"
    mkdir -p ~/Desktop/PC_SCAN
    if [ $? -ne 0 ]; then
        echo "Failed to make main Directory"
        exit 1
    fi
    cd ~/Desktop/PC_SCAN
    ls ~/Desktop/PC_SCAN/gitTraining
    if [ $? -ne 0 ]; then
        git clone https://github.com/YujiTheDragon/gitTraining.git
    fi
    $PYTHON_EXE -m ensurepip --upgrade
    pip install psutil
    pip install matplotlib
    if [ $? -ne 0 ]; then
        echo "Failed to download Modules"
        exit 1
    fi
    read -p "Press enter to continue"
    cd gitTraining/PythonT/OperatingSystemScan
    bash ./test.sh
fi
