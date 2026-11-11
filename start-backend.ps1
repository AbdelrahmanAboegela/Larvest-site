#!/usr/bin/env pwsh
# ============================================================
#  Larvest - Start Backend (Django) for Local Testing
#  Runs Django dev server with DEBUG=True on http://127.0.0.1:8000
# ============================================================

$venvPython = "$PSScriptRoot\Backend\LarvestVenv\Scripts\python.exe"
$backendDir  = "$PSScriptRoot\Backend"

if (-not (Test-Path $venvPython)) {
    Write-Error "Virtual environment not found at: $venvPython"
    Write-Host "Run: python -m venv Backend\LarvestVenv && Backend\LarvestVenv\Scripts\pip install -r Backend\requirements.txt"
    exit 1
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Starting Larvest Backend (Django)       " -ForegroundColor Green
Write-Host "  URL: http://127.0.0.1:8000              " -ForegroundColor Green
Write-Host "  API Docs: http://127.0.0.1:8000/        " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""

Push-Location $backendDir
try {
    $env:DJANGO_DEBUG = "True"
    & $venvPython manage.py runserver 127.0.0.1:8000
} finally {
    Pop-Location
}
