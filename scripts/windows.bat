@echo off
setlocal

for %%I in ("%~dp0..") do set "PROJECT_DIR=%%~fI"
set "PYTHON_EXE=%PROJECT_DIR%\.venv\Scripts\python.exe"
set "INSTALL_DIR=%LOCALAPPDATA%\Programs\timer"

if not exist "%PYTHON_EXE%" (
    echo Error: "%PYTHON_EXE%" was not found. Create the virtual environment first.
    exit /b 1
)

if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

(
    echo @echo off
    echo cd /d "%PROJECT_DIR%"
    echo "%PYTHON_EXE%" main.py
) > "%INSTALL_DIR%\timer.bat"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$installDir=$env:INSTALL_DIR; $userPath=[Environment]::GetEnvironmentVariable('Path','User'); if (($userPath -split ';') -notcontains $installDir) { if ([string]::IsNullOrWhiteSpace($userPath)) { $newPath=$installDir } else { $newPath=$userPath.TrimEnd(';') + ';' + $installDir }; [Environment]::SetEnvironmentVariable('Path',$newPath,'User') }"

if errorlevel 1 (
    echo Failed to add the timer command to your user PATH.
    exit /b 1
)

echo Installed successfully. Open a new terminal and run "timer".
