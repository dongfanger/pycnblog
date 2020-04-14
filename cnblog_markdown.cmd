@echo off
:start
set filePath=
set /p filePath=Please input file path:
python upload.py %filePath%
goto start