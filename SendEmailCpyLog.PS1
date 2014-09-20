$date = get-date -format yyyy-MM-dd

$EmailFrom = "sender@gmail.com"
$EmailTo = "recipient@gmail.com"
$Subject = "Morning Copy Report for $date"
TRY
{
    $Body = [IO.File]::ReadAllText("D:\Logs\log$date.txt")
}
    Catch
    {
        [system.exception]
        $Body = "No files were copied by move-torrents.bat"
    }
$SMTPServer = "smtp.gmail.com"
$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential("sender@gmail.com", "password");
$SMTPClient.Send($EmailFrom, $EmailTo, $Subject, $Body)