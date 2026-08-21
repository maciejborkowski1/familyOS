$root = $PSScriptRoot

$alreadyRunning = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object { $_.CommandLine -like "*bot.py*" }
if ($alreadyRunning) {
    exit
}

$logDir = Join-Path $root "logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }

Start-Process -FilePath "$root\venv\Scripts\python.exe" `
    -ArgumentList "`"$root\src\bot.py`"" `
    -RedirectStandardOutput (Join-Path $logDir "bot.out.log") `
    -RedirectStandardError (Join-Path $logDir "bot.log") `
    -WindowStyle Hidden
