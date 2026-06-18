#!/bin/bash

# Script para ejecutar Supermarket MT en macOS/Linux
# Uso: bash iniciar.sh o ./iniciar.sh

echo ""
echo "========================================"
echo "  SUPERMARKET MT - Sistema de Precios"
echo "========================================"
echo ""

# Cambiar a la carpeta del script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Verificar si Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "[1/4] ✗ ERROR: Python 3 no está instalado"
    echo "       En macOS: brew install python3"
    echo "       En Linux: sudo apt-get install python3 python3-venv"
    read -p "       Presiona Enter para salir"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1)
echo "[1/4] ✓ Python encontrado: $PYTHON_VERSION"

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "[2/4] Creando entorno virtual..."
    python3 -m venv venv
    echo "[2/4] ✓ Entorno virtual creado"
else
    echo "[2/4] ✓ Entorno virtual ya existe"
fi

# Activar entorno virtual
echo "[3/4] Activando entorno virtual..."
source venv/bin/activate
echo "[3/4] ✓ Entorno activado"

# Instalar dependencias
echo "[4/4] Instalando dependencias..."
pip install -q -r requirements.txt
echo "[4/4] ✓ Dependencias instaladas"

# Ejecutar aplicación
echo ""
echo "========================================"
echo "  ¡Aplicación iniciada!"
echo "========================================"
echo ""
echo "Abre tu navegador y ve a:"
echo "  http://localhost:5000"
echo ""
echo "Credenciales de admin:"
echo "  Usuario: admin"
echo "  PIN:     1234"
echo ""
echo "Presiona CTRL+C para detener la aplicación"
echo "========================================"
echo ""

python3 app.py
