@echo off
set filePath=
set /p filePath=Please input file path:
python upload.py %filePath%
pause