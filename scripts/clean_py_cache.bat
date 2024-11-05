@echo off
cd %~dp0



cd "..\"
echo "Delete cache folders in python folder ..."
for /d /r . %%d in (__pycache__) do @if exist "%%d" echo "%%d" && rd /s/q "%%d"
echo "Done"