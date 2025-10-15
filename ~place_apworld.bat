@echo off
setlocal

:: === CONFIGURATION ===
:: Name of the folder (in the current directory) you want to zip
set SOURCE_FOLDER=Pokeclicker-Apworld

:: Name for the zip/apworld file
set ZIP_NAME=Pokeclicker-Apworld

:: Destination folder where the .apworld should be moved
set DEST_FOLDER=H:\Emulation\Archipelago\custom_worlds

:: Program to run after moving the file
set PROGRAM_DIR=H:\Emulation\Archipelago
set PROGRAM_EXE=ArchipelagoGenerate.exe

:: === STEP 1: Compress the folder into a zip ===
:: Uses built-in Windows PowerShell to zip
powershell -command "Compress-Archive -Path '%SOURCE_FOLDER%' -DestinationPath '%ZIP_NAME%.zip' -Force"

:: === STEP 2: Rename the .zip to .apworld ===
ren "%ZIP_NAME%.zip" "%ZIP_NAME%.apworld"

:: === STEP 3: Move the .apworld to destination, overwrite if exists ===
move /Y "%ZIP_NAME%.apworld" "%DEST_FOLDER%\%ZIP_NAME%.apworld"

:: === STEP 4: Run the program from its directory ===
pushd "%PROGRAM_DIR%"
start "" "%PROGRAM_EXE%"
popd

endlocal
