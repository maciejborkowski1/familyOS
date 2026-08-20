$root = $PSScriptRoot

$alreadyRunning = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object { $_.CommandLine -like "*bot.py*" }
if ($alreadyRunning) {
    exit
}

$logDir = Join-Path $root "logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$log = Join-Path $logDir "bot.log"

& "$root\venv\Scripts\python.exe" "$root\src\bot.py" *>> $log
