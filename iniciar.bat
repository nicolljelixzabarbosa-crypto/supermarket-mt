@echo off
REM Script para ejecutar Supermarket MT en Windows
REM Crea automáticamente el entorno virtual si no existe

color 0A
title Supermarket MT - Sistema de Consulta de Precios

echo.
echo ========================================
echo   SUPERMARKET MT - Sistema de Precios
echo ========================================
echo.

REM Cambiar a la carpeta del script
cd /d "%~dp0"

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo ERROR: Python no está instalado o no está en PATH
    echo Descarga Python desde: https://www.python.org
    echo.
    pause
    exit /b 1
)

REM Crear entorno virtual si no existe
if not exist "venv" (
    echo [1/4] Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        color 0C
        echo ERROR: No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
    echo [1/4] ✓ Entorno virtual creado
) else (
    echo [1/4] ✓ Entorno virtual ya existe
)

REM Activar entorno virtual
echo [2/4] Activando entorno virtual...
call venv\Scripts\activate.bat
echo [2/4] ✓ Entorno virtual activado

REM Instalar dependencias
echo [3/4] Instalando dependencias...
pip install -q -r requirements.txt
if errorlevel 1 (
    color 0C
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo [3/4] ✓ Dependencias instaladas

REM Ejecutar la aplicación
echo [4/4] Iniciando aplicación...
echo.
color 0B
echo ========================================
echo   ¡Aplicación iniciada!
echo ========================================
echo.
echo Abre tu navegador y ve a:
echo   http://localhost:5000
echo.
echo Credenciales de admin:
echo   Usuario: admin
echo   PIN:     1234
echo.
echo Presiona CTRL+C para detener la aplicación
echo ========================================
echo.

python app.py

REM Si llega aquí, la app terminó
color 0E
echo.
echo Aplicación cerrada.
pause
