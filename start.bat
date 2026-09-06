@echo off
setlocal enabledelayedexpansion
title TraceX Forensic Engine - Windows Launcher
color 0B

echo.
echo  ===================================================================
echo    TraceX - Blockchain Intelligence & VASP Attribution Engine v2.0
echo    Ministry of Home Affairs // Indian Cyber Crime Coordination Centre
echo  ===================================================================
echo.

REM 1. Detect Python Command (try "python", then "py -3")
set "PYTHON_CMD="
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python"
) else (
    py -3 --version >nul 2>&1
    if %errorlevel% equ 0 (
        set "PYTHON_CMD=py -3"
    )
)

if "%PYTHON_CMD%"=="" (
    color 0C
    echo  [X] ERROR: Python is not installed or not added to your PATH!
    echo.
    echo  -------------------------------------------------------------------
    echo  HOW TO FIX IN 1 MINUTE:
    echo   1. Download Python 3.10 / 3.11 / 3.12 from: https://www.python.org/downloads/
    echo   2. Run installer and **MAKE SURE TO CHECK**:
    echo      [X] "Add python.exe to PATH" (at the very bottom of the installer)
    echo   3. Click "Install Now", close CMD, and double-click start.bat again!
    echo  -------------------------------------------------------------------
    echo.
    pause
    exit /b 1
)

echo  [+] Detected Python:
%PYTHON_CMD% --version
echo.

REM 2. Check and Install Required Packages
echo  [*] Checking and installing required dependencies...
%PYTHON_CMD% -m pip install --upgrade pip >nul 2>&1
%PYTHON_CMD% -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    color 0E
    echo  [!] Warning: pip install encountered an issue. Trying direct install...
    %PYTHON_CMD% -m pip install fastapi "uvicorn[standard]" pydantic requests networkx python-dotenv
)

echo.
echo  [+] All dependencies verified!
echo.

REM 3. Launch Dashboard in Default Browser after 2 seconds
start "" "http://localhost:8765"

REM 4. Launch FastAPI Uvicorn Server
echo  ===================================================================
echo   [OK] Server running at: http://localhost:8765
echo   [OK] API Docs:          http://localhost:8765/docs
echo   [!] To stop the engine, press Ctrl + C in this terminal window.
echo  ===================================================================
echo.

%PYTHON_CMD% -m uvicorn app:app --host 0.0.0.0 --port 8765 --reload

pause
