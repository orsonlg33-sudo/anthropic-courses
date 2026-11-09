$root = (git rev-parse --show-toplevel).Trim()
Set-Location $root
$failed = $false

# Check 1: no .env files tracked by git
$envFiles = git ls-files | Where-Object { $_ -match '(^|/)\.env($|\.)' -and $_ -notmatch '\.env\.example$' }
if ($envFiles) {
    Write-Output "FAIL: tracked .env files:"
    $envFiles | ForEach-Object { Write-Output "  $_" }
    $failed = $true
} else {
    Write-Output "PASS: no .env files are tracked"
}

# Check 2: no text that looks like an API key in tracked files
$pattern = 'sk-' + 'ant|pa-[A-Za-z0-9]{20,}'
$hits = git grep -I -n -E $pattern
if ($hits) {
    Write-Output "FAIL: possible API keys found:"
    $hits | ForEach-Object { Write-Output "  $_" }
    $failed = $true
} else {
    Write-Output "PASS: no API key patterns in tracked files"
}

# Check 3: no BOM (UTF-8 or UTF-16) at the start of tracked text files
$bom = @()
foreach ($f in (git ls-files)) {
    if ($f -match '\.(md|py|json|txt|toml|csv)$' -and (Test-Path -LiteralPath $f)) {
        $fs = [System.IO.File]::OpenRead((Join-Path $root $f))
        $buf = New-Object byte[] 3
        $n = $fs.Read($buf, 0, 3)
        $fs.Close()
        $utf8 = ($n -eq 3 -and $buf[0] -eq 239 -and $buf[1] -eq 187 -and $buf[2] -eq 191)
        $utf16 = ($n -ge 2 -and (($buf[0] -eq 255 -and $buf[1] -eq 254) -or ($buf[0] -eq 254 -and $buf[1] -eq 255)))
        if ($utf8 -or $utf16) { $bom += $f }
    }
}
if ($bom.Count -gt 0) {
    Write-Output "FAIL: files starting with a BOM:"
    $bom | ForEach-Object { Write-Output "  $_" }
    $failed = $true
} else {
    Write-Output "PASS: no BOM in tracked text files"
}

if ($failed) { Write-Output "RESULT: FAIL"; exit 1 } else { Write-Output "RESULT: PASS"; exit 0 }