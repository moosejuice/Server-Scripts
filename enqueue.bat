move "E:\Working\To Convert\*.avi" "E:\Working\Converting\"
move "E:\Working\To Convert\"*.mkv "E:\Working\Converting\"
FOR /F "tokens=*" %%G IN ('DIR /B /S *.avi') DO "C:\Program Files\Handbrake\HandBrakeCLI" -i "%%G" -o "%%G".mp4 --preset="AppleTV 3"
FOR /F "tokens=*" %%G IN ('DIR /B /S *.mkv') DO "C:\Program Files\Handbrake\HandBrakeCLI" -i "%%G" -o "%%G".mp4 --preset="AppleTV 3"
move E:\Working\Converting\*.mp4 E:\Working\Converted\
attrib -r /S
del E:\Working\Converting\*.mkv
del E:\Working\Converting\*.avi
cd /d C:\
cd Scripts
tag_videos.bat