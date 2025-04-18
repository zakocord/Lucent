@echo off
color 6
echo WARNING: Skipping this installation may result in tools, etc. not working.

pip install -r requirements.txt
py build.py
pause
