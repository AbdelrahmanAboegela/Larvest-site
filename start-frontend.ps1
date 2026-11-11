#!/usr/bin/env pwsh
# ============================================================
#  Larvest - Start Frontend (Next.js) for Local Testing
#  Runs Next.js dev server on http://localhost:3000
#  API calls are proxied to http://127.0.0.1:8000 automatically
# ============================================================

$frontendDir = "$PSScriptRoot\Frontend"

if (-not (Test-Path "$frontendDir\node_modules")) {
    Write-Host "node_modules not found. Installing dependencies..." -ForegroundColor Yellow
    Push-Location $frontendDir
    npm install
    Pop-Location
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Starting Larvest Frontend (Next.js)     " -ForegroundColor Cyan
Write-Host "  URL: http://localhost:3000              " -ForegroundColor Cyan
Write-Host "  API Proxy → http://127.0.0.1:8000      " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

Push-Location $frontendDir
try {
    npm run dev
} finally {
    Pop-Location
}
