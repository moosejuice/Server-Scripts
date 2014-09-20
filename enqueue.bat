move "E:\Working\To Convert\*.avi" "E:\Working\Converting\"
move "E:\Working\To Convert\"*.mkv "E:\Working\Converting\"
FOR /F "tokens=*" %%G IN ('DIR /B /S *.avi') DO "C:\Program Files\Handbrake\HandBrakeCLI" -i "%%G" -o "E:\Working\Done""%%G".mp4 --preset="AppleTV 3"
FOR /F "tokens=*" %%G IN ('DIR /B /S *.mkv') DO "C:\Program Files\Handbrake\HandBrakeCLI" -i "%%G" -o "E:\Working\Done""%%G".mp4 --preset="AppleTV 3"
move E:\Working\Done\*.* E:\Working\Converted\