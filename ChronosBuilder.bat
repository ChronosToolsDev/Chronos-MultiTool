@echo off
setlocal EnableDelayedExpansion
cd /d "%~dp0"

REM ============================================================
REM  Chronos Builder — Free Edition bootstrap launcher
REM  ============================================================
REM  On first run:
REM    - Creates a local runtime\ folder next to this batch
REM    - Downloads Python 3.11 embeddable + pip
REM    - pip installs the required packages into runtime\
REM    - Launches chronos_builder-free.py
REM  On subsequent runs:
REM    - Reuses the local runtime\, launches the builder immediately
REM  ============================================================

set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"
set "RUNTIME=%ROOT%\runtime"
set "PY=%RUNTIME%\python.exe"
set "PY_VER=3.11.9"
set "PY_URL=https://www.python.org/ftp/python/%PY_VER%/python-%PY_VER%-embed-amd64.zip"
set "GETPIP_URL=https://bootstrap.pypa.io/get-pip.py"
set "BUILDER=%ROOT%\chronos_builder-free.py"

REM --- sanity check ---
if not exist "%BUILDER%" (
    echo [X] chronos_builder-free.py not found in:
    echo     %ROOT%
    echo.
    echo     Put this batch in the same folder as the builder.
    pause
    exit /b 1
)

REM --- first-run bootstrap ---
if not exist "%PY%" (
    echo ============================================================
    echo  First-run setup
    echo ============================================================
    echo.
    echo [*] Creating local runtime folder...
    if not exist "%RUNTIME%" mkdir "%RUNTIME%"

    echo [*] Downloading Python %PY_VER% embeddable...
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
        "$ProgressPreference='SilentlyContinue';" ^
        "try {" ^
        "  Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%RUNTIME%\python.zip' -UseBasicParsing;" ^
        "} catch {" ^
        "  Write-Host '[X] Download failed:' $_.Exception.Message;" ^
        "  exit 1" ^
        "}"
    if errorlevel 1 (
        echo [X] Failed to download Python. Check your internet connection.
        pause
        exit /b 1
    )

    echo [*] Extracting Python...
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
        "Expand-Archive -Path '%RUNTIME%\python.zip' -DestinationPath '%RUNTIME%' -Force"
    if errorlevel 1 (
        echo [X] Failed to extract Python.
        pause
        exit /b 1
    )
    del /q "%RUNTIME%\python.zip" >nul 2>&1

    echo [*] Enabling site-packages in the embeddable runtime...
    REM The embeddable Python has a ._pth file that disables site imports.
    REM Uncomment the "import site" line so pip-installed packages are found.
    for %%F in ("%RUNTIME%\python*._pth") do (
        powershell -NoProfile -ExecutionPolicy Bypass -Command ^
            "$f='%%~fF';" ^
            "$lines = Get-Content $f;" ^
            "$lines = $lines -replace '^#\s*import site', 'import site';" ^
            "$lines = $lines -replace '^#import site', 'import site';" ^
            "Set-Content -Path $f -Value $lines -Encoding ASCII"
    )

    echo [*] Downloading get-pip.py...
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
        "$ProgressPreference='SilentlyContinue';" ^
        "try {" ^
        "  Invoke-WebRequest -Uri '%GETPIP_URL%' -OutFile '%RUNTIME%\get-pip.py' -UseBasicParsing;" ^
        "} catch {" ^
        "  Write-Host '[X] Download failed:' $_.Exception.Message;" ^
        "  exit 1" ^
        "}"
    if errorlevel 1 (
        echo [X] Failed to download get-pip.py.
        pause
        exit /b 1
    )

    echo [*] Installing pip...
    "%PY%" "%RUNTIME%\get-pip.py" --no-warn-script-location
    if errorlevel 1 (
        echo [X] pip installation failed.
        pause
        exit /b 1
    )
    del /q "%RUNTIME%\get-pip.py" >nul 2>&1

    echo.
    echo [*] Installing builder dependencies...
    "%PY%" -m pip install --no-warn-script-location ^
        "pyinstaller>=6.0" ^
        "pywin32>=306" ^
        "pycryptodome>=3.19" ^
        "Pillow>=10.0" ^
        "requests>=2.31" ^
        "psutil>=5.9" ^
        "colorama>=0.4.6"
    if errorlevel 1 (
        echo [X] Dependency installation failed.
        pause
        exit /b 1
    )

    echo.
    echo [V] Setup complete.
    echo.
)

REM --- launch the builder ---
title Chronos Builder - Free Edition
"%PY%" "%BUILDER%"

REM --- post-exit ---
echo.
echo [*] Builder exited.
pause
exit /b 0
