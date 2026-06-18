# 🛒 Supermarket MT - Sistema de Consulta de Precios

Un sistema web profesional y fácil de usar para consultar precios en un supermercado local. Desarrollado con Python + Flask + SQLite.

---

## 📋 Características

✅ **Consulta de Precios**: Escanea códigos de barras o busca por nombre  
✅ **Detección Automática**: Detecta si se usa cámara o lector de barras  
✅ **Panel Admin**: Agregar, editar y eliminar productos  
✅ **Autenticación**: Sistema de PIN para administrador  
✅ **Interfaz Bonita**: Diseño profesional con colores de supermercado  
✅ **Responsive**: Funciona en PC, tablet y celular  
✅ **Independiente**: Funciona sin conexión a internet  
✅ **Base de Datos**: SQLite automática y portátil  

---

## 🛠️ Requisitos Previos

- **Python 3.7 o superior** (descargar desde [python.org](https://www.python.org))
- **pip** (gestor de paquetes de Python)
- **Un navegador moderno** (Chrome, Firefox, Edge, Safari)

---

## 📦 Instalación y Configuración

### Paso 1: Clonar o descargar el proyecto

```bash
# Si tienes Git, clonar el repositorio:
git clone <URL-del-repositorio>
cd supermarket-mt

# O simplemente descargar como ZIP y extraer
```

### Paso 2: Crear un entorno virtual (recomendado)

```bash
# En Windows:
python -m venv venv
venv\Scripts\activate

# En macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecutar la Aplicación

### Método 1: Desde la terminal

```bash
# Asegúrate de estar en la carpeta del proyecto
cd supermarket-mt

# Activar el entorno virtual (si lo creaste)
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Ejecutar la aplicación
python app.py
```

Verás algo como esto:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: ON
```

### Método 2: Crear un archivo de acceso rápido (Windows)

Crea un archivo llamado `iniciar.bat` en la carpeta del proyecto:

```batch
@echo off
cd /d "%~dp0"
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -r requirements.txt
python app.py
pause
```

Luego solo haz doble clic en `iniciar.bat` para ejecutar.

---

## 🌐 Acceder a la Aplicación

1. Abre tu navegador favorito
2. Ingresa la siguiente URL:
   - **En tu PC**: `http://localhost:5000`
   - **Desde otro dispositivo en la red**: `http://<IP-DE-TU-PC>:5000`
     
   Para encontrar tu IP, en terminal escribe: `ipconfig` (Windows) o `ifconfig` (macOS/Linux)

---

## 👤 Credenciales de Acceso

### Acceso de Admin:

Se crea automáticamente en la primera ejecución.

**Para cambiar la contraseña de forma segura:**

```bash
python cambiar_contraseña.py
```

Te pedirá:
1. Contraseña actual (deja en blanco la primera vez)
2. Nueva contraseña (oculta mientras escribes)
3. Confirmar contraseña

---

## 📱 Uso de la Aplicación

### 🔍 **Página Principal - Consultar Precio**

1. El campo de búsqueda estará con autofocus
2. Escanea un código de barras o escribe el nombre del producto
3. El sistema detectará automáticamente si es un lector o búsqueda manual
4. Presiona **Enter** para buscar
5. Verás el precio y detalles del producto

### ⚙️ **Panel de Admin**

1. Haz clic en **Admin** en la esquina superior derecha
2. Ingresa usuario y contraseña
3. En el panel verás:
   - ➕ **Agregar producto**: Escanea código, ingresa nombre y precio
   - 📋 **Lista de productos**: Ver todos los registros
   - ✏️ **Editar**: Actualiza datos del producto
   - 🗑️ **Eliminar**: Borra un producto

---

## 💾 Base de Datos

El archivo `supermarket.db` se crea automáticamente en la primera ejecución.

**Ubicación**: `<carpeta-del-proyecto>/supermarket.db`

**Para respaldar**: Solo copia el archivo `supermarket.db` a un lugar seguro.

**Para restaurar**: Reemplaza el archivo `supermarket.db` con tu backup.

---

## 🔧 Troubleshooting

### ❌ Error: "No module named 'flask'"

```bash
pip install -r requirements.txt
```

### ❌ Puerto 5000 ya está en uso

Modifica el puerto en `app.py` línea final:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Cambiar 5000 por otro número
```

### ❌ La aplicación se cierra inmediatamente

Verifica que:
1. Python está instalado: `python --version`
2. Estás en la carpeta correcta
3. Las dependencias están instaladas: `pip install -r requirements.txt`

### ❌ No veo la base de datos

La base de datos se crea automáticamente en la primera ejecución. Si no aparece:

1. Verifica permisos de escritura en la carpeta
2. Ejecuta: `python database.py` para inicializarla manualmente

---

## 📂 Estructura del Proyecto

```
supermarket-mt/
├── app.py                 # Backend Flask (rutas y lógica)
├── database.py            # Gestión de SQLite
├── requirements.txt       # Dependencias Python
├── supermarket.db         # Base de datos (se crea automáticamente)
├── static/
│   ├── css/
│   │   └── style.css      # Estilos (tema supermercado)
│   ├── js/
│   │   └── scanner.js     # Detección automática de lectura
│   └── img/               # Imágenes y iconos
└── templates/
    ├── base.html          # Plantilla base (footer, navegación)
    ├── consultar.html     # Página principal (búsqueda)
    ├── admin.html         # Panel de administración
    └── login_admin.html   # Pantalla de login
```

---

## 🌐 Subir a la Nube (Opcional)

Para que funcione sin tu presencia, puedes subirlo a:

- **Heroku** (gratis, con limitaciones)
- **PythonAnywhere** (hosting específico para Python)
- **AWS** o **Google Cloud** (con más control)
- **Un servidor VPS** (cPanel, etc.)

---

## 📝 Notas Importantes

- ✅ El footer con el crédito "Sistema desarrollado por: Nicoll Jelixza Barbosa Matallana" está en todas las páginas
- ✅ El sistema detecta automáticamente si es un lector de barras o entrada manual
- ✅ El autofocus mantiene el cursor en el buscador
- ✅ Los datos se guardan en SQLite (portátil y confiable)
- ✅ La interfaz es responsive para móviles, tablets y PC

---

## 🤝 Soporte y Dudas

Si tienes problemas:

1. Verifica que Python esté instalado correctamente
2. Asegúrate de estar en la carpeta correcta
3. Instala las dependencias: `pip install -r requirements.txt`
4. Revisa los logs en la terminal

---

## 📄 Créditos

**Sistema desarrollado por: Nicoll Jelixza Barbosa Matallana**

**Proyecto para**: Supermarket MT (Supermercado local)

---

¡Listo para usar! 🎉
