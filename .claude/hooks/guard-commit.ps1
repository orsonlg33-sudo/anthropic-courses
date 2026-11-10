$raw = [Console]::In.ReadToEnd()
$data = $raw | ConvertFrom-Json
$cmd = $data.tool_input.command

if ($cmd -match '\bgit\s+(commit|push)\b') {
    $check = Join-Path $PSScriptRoot "..\skills\verify-repo\check.ps1"
    $out = & powershell -File $check 2>&1
    if ($LASTEXITCODE -ne 0) {
        [Console]::Error.WriteLine("Blocked: repo verification failed.`n" + ($out -join "`n"))
        exit 2
    }
}
exit 0