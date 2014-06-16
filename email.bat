@echo OFF

copy D:\Logs\log%date%.txt C:\Scripts\log.txt


timeout /t 5

start "C:\Scripts" sendEmail.exe -s smtp.gmail.com:587 -f something@gmail.com -xu something@gmail.com -xp password -o tls=yes -t Recipient@gmail.com -u File Copy Logs for %date% -m See attached log files -a log.txt

echo Y | del log.txt


