# 🛒 SUPERMARKET MT - GUÍA RÁPIDA DE INSTALACIÓN

## ✅ Paso 1: Verificar Python

Abre una terminal/PowerShell y ejecuta:

```bash
python --version
```

Si no ves la versión, **descarga Python** desde: https://www.python.org

---

## ✅ Paso 2: Instalar dependencias

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

---

## ✅ Paso 3: EJECUTAR LA APLICACIÓN

### 🪟 **En Windows:**

**Opción A - Más fácil (Doble clic):**
- Haz doble clic en el archivo **`iniciar.bat`**
- Se abrirá una terminal automáticamente
- La aplicación estará lista en segundos

**Opción B - PowerShell:**
```bash
powershell -ExecutionPolicy Bypass -File iniciar.ps1
```

**Opción C - Terminal/CMD manual:**
```bash
python app.py
```

### 🍎 **En macOS/Linux:**

**Opción A - Script automático:**
```bash
bash iniciar.sh
```

O dame permisos de ejecución primero:
```bash
chmod +x iniciar.sh
./iniciar.sh
```

**Opción B - Manual:**
```bash
python3 -m venv venv
source venv/bin/activate  # En macOS/Linux
pip install -r requirements.txt
python3 app.py
```

---

## 🌐 Acceder a la aplicación

Una vez que ves en la terminal:
```
* Running on http://127.0.0.1:5000
```

Abre tu navegador y ve a:
### 👉 **http://localhost:5000**

---

## 🔐 Credenciales de Admin

La contraseña predeterminada se crea automáticamente en la primera ejecución.

**Para cambiar la contraseña:**

```bash
python cambiar_contraseña.py
```

Te pedirá:
1. Contraseña actual (deja en blanco si es la primera vez)
2. Nueva contraseña
3. Confirmar nueva contraseña

**La contraseña será oculta mientras escribes** (por seguridad)

---

## 📱 Funcionalidades

### 🔍 **Página Principal**
- Escanea códigos de barras
- Busca por nombre de producto
- El sistema detecta automáticamente si es un lector

### ⚙️ **Panel Admin**
- Agregar productos
- Editar precios y datos
- Eliminar productos
- Ver lista completa

---

## 💡 Consejos Importantes

1. **Autofocus**: El buscador siempre está activo (listo para escanear)
2. **Lector de barras**: Conecta un lector a la tablet/PC
3. **Respaldos**: Copia el archivo `supermarket.db` para respaldar datos
4. **Desde otro dispositivo**: Usa `http://<IP-DE-TU-PC>:5000`
   - Para saber tu IP: escribe `ipconfig` en CMD

---

## ⚡ Troubleshooting Rápido

| Problema | Solución |
|----------|----------|
| "No module named 'flask'" | `pip install -r requirements.txt` |
| Puerto 5000 en uso | Edita `app.py` última línea, cambia 5000 por 5001 |
| La app se cierra | Verifica Python: `python --version` |
| Permisos denegados (Linux) | `chmod +x iniciar.sh` |

---

## 🎯 ¡Listo!

Ahora tienes un sistema profesional para tu supermercado.

**Sistema desarrollado por: Nicoll Jelixza Barbosa Matallana**

¡Éxito! 🎉
