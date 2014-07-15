@echo off
setlocal enabledelayedexpansion
FOR /F "delims=*" %%G IN ('DIR /B /S "E:\Working\Converted\*.m4a"') DO (
"C:\Scripts\ffmpeg.exe" -i "%%G" -ab 256k "E:\Working\Converted\%%~nG.mp3"
del "%%G"
move "E:\Working\Converted\%%~nG.mp3" "D:\Library\Automatically Add to iTunes\"
)

FOR /F "delims=*" %%G IN ('DIR /B /S "E:\Working\Converted\*.flac"') DO (
"C:\Scripts\ffmpeg.exe" -i "%%G" -ab 256k "E:\Working\Converted\%%~nG.mp3"
del "%%G"
move "E:\Working\Converted\%%~nG.mp3" "D:\Library\Automatically Add to iTunes\"
)

python C:\Scripts\organize_mp3.py