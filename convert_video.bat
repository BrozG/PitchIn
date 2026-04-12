@echo off
REM Convert readme-intro.mp4 to GIF for better README display
REM Requires ffmpeg installed

set INPUT=resource\readme-intro.mp4
set OUTPUT=resource\demo.gif

echo 🎬 Converting video to GIF...

if not exist "%INPUT%" (
    echo ❌ Input file not found: %INPUT%
    exit /b 1
)

REM Check if ffmpeg is installed
where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo ❌ ffmpeg is not installed. Please install it first:
    echo    Download from https://ffmpeg.org/download.html
    echo    Or use winget: winget install Gyan.FFmpeg
    exit /b 1
)

REM Convert to GIF (optimized for README display)
ffmpeg -i "%INPUT%" ^
  -vf "fps=10,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" ^
  -loop 0 ^
  "%OUTPUT%"

if %errorlevel% equ 0 (
    echo ✅ Successfully created: %OUTPUT%
    for /f "tokens=*" %%i in ('powershell -Command "(Get-Item '%OUTPUT%').Length / 1KB"') do set SIZE=%%i
    echo 📏 Size: %SIZE% KB
    echo 📋 Update your README.md to use:
    echo    ^<img src="%OUTPUT%" alt="Pitch In Demo" width="800" /^>
) else (
    echo ❌ Conversion failed
    exit /b 1
)