# SKAO timer

## Overview
This project is a simple command line timer for Suankularb Wittayalai School's astronomy olympiad camp. The time for each station is hardwired to be 5 minutes, with 1-minute-remaining alert. If you find any bug or have any question, feel free to contact the developer at email boonyakorn.tha@gmail.com

## How to install and run
### Install as a standalone program for Windows
Please refer to [windows_exe branch](https://github.com/polya2005/SKAO-timer/tree/windows_exe)

### Install and run with Python
1. Download and install Python from [the official Python website](https://www.python.org)
    - For Windows, do not forget to add python.exe to `PATH` variable.
2. Install the `playsound` package
    - For Windows, install version `1.2.2` using the following command, with command prompt run as administrator.

        ```pip install playsound==1.2.2```
    
    > [!IMPORTANT] 
    > At the time of testing, the latest version does not work on Windows. Therefore, `==1.2.2` is required.

    - For macOS and Linux, install the latest version using the following command.

        ```pip3 install playsound```
3. Download the files `main.py`, `nextround.mp3`, `oneminleft.mp3`, and `timeout.mp3`. Place them in the same folder.
4. Run `main.py`
    - For Windows, use the following command.
        ```python main.py```
    - For macOS and Linux, use the following command.
        ```python3 main.py```