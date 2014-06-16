$date = get-date -format F

$EmailFrom = "sender@gmail.com”
$EmailTo = "recipient@gmail.com"
$Subject = “Administrator login on Charon $date”
$body = "Administrator on Charon has just signed on. Here are the last 5 power off details..`r`r"
$i=0
$myVar = Get-WinEvent -FilterHashtable @{logname='System'; id=1074}  |
ForEach-Object {
if($i -lt 5)
{


$rv = New-Object PSObject | Select-Object Date, User, Action, Process, Reason, ReasonCode, Comment
$rv.Date = $_.TimeCreated
$rv.User = $_.Properties[6].Value
$rv.Process = $_.Properties[0].Value
$rv.Action = $_.Properties[4].Value
$rv.Reason = $_.Properties[2].Value
$rv.ReasonCode = $_.Properties[3].Value
$rv.Comment = $_.Properties[5].Value
$rv
}
$i++
    
} | Select-Object Date, Action, Reason, User | Out-String
$body = $body + $myVar
echo $body
$SMTPServer = “smtp.gmail.com”
$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential("sender@gmail.com", "password");
$SMTPClient.Send($EmailFrom, $EmailTo, $Subject, $Body)