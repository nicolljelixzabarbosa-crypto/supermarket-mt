# Script PowerShell para ejecutar Supermarket MT
# Uso: powershell -ExecutionPolicy Bypass -File iniciar.ps1

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  SUPERMARKET MT - Sistema de Precios" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green

# Cambiar a la carpeta del script
$ScriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptPath

# Verificar si Python está instalado
try {
    $PythonVersion = python --version 2>&1
    Write-Host "[1/4] ✓ Python encontrado: $PythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "[1/4] ✗ ERROR: Python no está instalado" -ForegroundColor Red
    Write-Host "       Descarga Python desde: https://www.python.org" -ForegroundColor Yellow
    Read-Host "       Presiona Enter para salir"
    exit 1
}

# Crear entorno virtual si no existe
if (-not (Test-Path "venv")) {
    Write-Host "[2/4] Creando entorno virtual..." -ForegroundColor Cyan
    python -m venv venv
    Write-Host "[2/4] ✓ Entorno virtual creado" -ForegroundColor Green
}
else {
    Write-Host "[2/4] ✓ Entorno virtual ya existe" -ForegroundColor Green
}

# Activar entorno virtual
Write-Host "[3/4] Activando entorno virtual..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"
Write-Host "[3/4] ✓ Entorno activado" -ForegroundColor Green

# Instalar dependencias
Write-Host "[4/4] Instalando dependencias..." -ForegroundColor Cyan
pip install -q -r requirements.txt
Write-Host "[4/4] ✓ Dependencias instaladas" -ForegroundColor Green

# Ejecutar aplicación
Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  ¡Aplicación iniciada!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Abre tu navegador y ve a:" -ForegroundColor Yellow
Write-Host "  http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Credenciales de admin:" -ForegroundColor Yellow
Write-Host "  Usuario: admin" -ForegroundColor Cyan
Write-Host "  PIN:     1234" -ForegroundColor Cyan
Write-Host ""
Write-Host "Presiona CTRL+C para detener la aplicación" -ForegroundColor Yellow
Write-Host "========================================`n" -ForegroundColor Green

python app.py
