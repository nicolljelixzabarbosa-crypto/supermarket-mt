# 🚀 CÓMO EJECUTAR SUPERMARKET MT

## OPCIÓN 1: Windows - La Más Fácil ⭐

### Paso 1: Abre la carpeta
```
C:\Users\chomi\OneDrive\Practica\supermarket-mt
```

### Paso 2: Doble clic en `iniciar.bat`
- Verás una terminal negra
- El script creará el entorno virtual automáticamente
- Instalará las dependencias
- Ejecutará la aplicación

### Paso 3: Abre tu navegador
```
http://localhost:5000
```

**¡Listo! Ya está funcionando!**

---

## OPCIÓN 2: Terminal/CMD (Cualquier Sistema)

### Paso 1: Abre terminal en la carpeta del proyecto

```bash
# Navega a la carpeta
cd C:\Users\chomi\OneDrive\Practica\supermarket-mt

# En Windows con PowerShell, ejecuta:
powershell -ExecutionPolicy Bypass -File iniciar.ps1

# O simplemente:
python app.py
```

### Paso 2: Si es la primera vez, instala dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecuta la app

```bash
python app.py
```

Verás en la terminal:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: ON
```

### Paso 4: Abre el navegador

```
http://localhost:5000
```

---

## OPCIÓN 3: macOS / Linux

### Terminal:

```bash
cd ~/path/to/supermarket-mt

# Ejecutar el script automático:
bash iniciar.sh

# O manual:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

---

## 🎯 QUÉ VER EN EL NAVEGADOR

### Página 1: Consultar Precio
- Campo de búsqueda con autofocus
- Escanea código o escribe nombre
- Presiona Enter
- ¡Ver el precio al instante!

### Página 2: Panel Admin
- Clic en "Admin"
- Ingresa usuario: `admin`
- Ingresa PIN: `1234`
- Agrega, edita, elimina productos

---

## 🔗 URLs

- **Principal**: http://localhost:5000
- **Admin**: http://localhost:5000/admin
- **Login Admin**: http://localhost:5000/login_admin

---

## 📊 Cargar Datos de Ejemplo

Si quieres agregar 23 productos de ejemplo:

```bash
python cargar_datos_ejemplo.py
```

Luego ejecuta:

```bash
python app.py
```

---

## 🛑 Detener la Aplicación

En la terminal donde está ejecutando:

```
Presiona: CTRL + C
```

---

## ❓ Si No Funciona

### Error 1: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error 2: "Port 5000 already in use"
Edita `app.py`, última línea:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambiar 5000 a 5001
```

### Error 3: "Python no encontrado"
1. Descarga Python desde https://www.python.org
2. Instala con "Add Python to PATH" ✓
3. Reinicia la terminal

### Error 4: "Permiso denegado" (Linux/macOS)
```bash
chmod +x iniciar.sh
./iniciar.sh
```

---

## 📱 Acceder desde Otro Dispositivo

1. En Windows, abre CMD/PowerShell
2. Ejecuta: `ipconfig`
3. Busca: "IPv4 Address" (ej: 192.168.1.100)
4. En otro dispositivo, ve a: `http://192.168.1.100:5000`

---

## 💡 Tips Profesionales

- **Autofocus**: El campo de búsqueda siempre está listo
- **Lector de barras**: Conecta USB → automáticamente funciona
- **Datos seguros**: Copia `supermarket.db` para respaldar
- **Cambiar puerto**: Modifica última línea de `app.py`
- **Cambiar colores**: Edita `static/css/style.css`

---

## ✨ Ejemplos de Uso

### Búsqueda por código
```
1234567890 + Enter → Muestra: Agua Mineral 500ml - $1.50
```

### Búsqueda por nombre
```
Leche + Enter → Muestra: Leche Entera 1L - $2.80
```

### Panel Admin
```
Usuario: admin
PIN: 1234
→ Agregar "Pan" - Código: 9999999999 - Precio: $2.50
```

---

## 🎉 ¡Éxito!

Ya tienes tu sistema profesional de supermercado corriendo.

**Recuerda:**
- 🔐 Admin: usuario `admin`, PIN `1234`
- 📝 Footer: Nicoll Jelixza Barbosa Matallana
- 💾 Datos: Guardados automáticamente en `supermarket.db`

---

**¡Tu supermercado está listo! 🛒**
