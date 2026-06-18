# 🚀 GUÍA: SUBIR A RAILWAY (Hosting en la Nube)

## ¿Qué es Railway?
Un hosting donde tu app funciona **24/7** sin necesidad de tu portátil. La tablet del local accede desde cualquier lugar.

---

## 📋 REQUISITOS PREVIOS

1. **Cuenta GitHub** (gratis): https://github.com
2. **Cuenta Railway** (gratis): https://railway.app
3. **Git instalado**: https://git-scm.com

---

## 🎯 PASO 1: Preparar tu Computadora

### 1.1 Instalar Git (si no lo tienes)
```bash
# Descarga desde: https://git-scm.com
# Instala con opciones por defecto
```

### 1.2 Verifica que Git esté instalado
```bash
git --version
```

---

## 📂 PASO 2: Crear Repositorio GitHub

### 2.1 Crear cuenta en GitHub
- Ve a https://github.com
- Clic en "Sign up"
- Usa tu correo de Google (más fácil)

### 2.2 Crear nuevo repositorio
- Clic en "+" → "New repository"
- Nombre: `supermarket-mt`
- Descripción: `Sistema de consulta de precios para supermercado`
- ✓ "Public" (así Railway lo ve)
- Clic en "Create repository"

---

## 💻 PASO 3: Subir Proyecto a GitHub

Abre PowerShell en tu carpeta del proyecto:

```bash
cd C:\Users\chomi\OneDrive\Practica\supermarket-mt
```

Ejecuta estos comandos **UNO POR UNO**:

```bash
# 1. Inicializar git
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@gmail.com"

# 2. Crear repositorio local
git init

# 3. Agregar todos los archivos
git add .

# 4. Hacer commit
git commit -m "Supermarket MT - Sistema de Precios"

# 5. Renombrar rama a main
git branch -M main

# 6. Agregar remoto (CAMBIA tu-usuario por tu username GitHub)
git remote add origin https://github.com/tu-usuario/supermarket-mt.git

# 7. Subir a GitHub
git push -u origin main
```

**Nota:** En el paso 7 te pedirá autenticación:
- Si tienes GitHub Desktop instalado, autoriza ahí
- Si no, crea un token en GitHub y úsalo como contraseña

---

## 🚀 PASO 4: Conectar con Railway

### 4.1 Crear cuenta Railway
- Ve a https://railway.app
- Clic en "Start Project"
- Selecciona "Deploy from GitHub" 
- Autoriza Railway
- Selecciona el repositorio `supermarket-mt`

### 4.2 Railway Detecta y Despliega
- Railway ve que es Python (por `requirements.txt`)
- Lee `Procfile` y `runtime.txt`
- ¡**Despliega automáticamente!**

### 4.3 Obtener tu URL
- En Railway, ve a "Settings"
- Busca "Domains"
- Copiar el dominio (algo como: `supermarket-mt-production.up.railway.app`)

---

## 🌐 PASO 5: Usar en la Tablet

En la tablet, abre navegador y escribe:

```
https://supermarket-mt-production.up.railway.app
```

**(Reemplaza con tu URL real de Railway)**

¡**Funciona!** 🎉

---

## 📊 RESUMEN RÁPIDO

| Paso | Acción |
|------|--------|
| 1 | Crear cuenta GitHub |
| 2 | Crear repositorio GitHub |
| 3 | `git push` tu código a GitHub |
| 4 | Crear cuenta Railway |
| 5 | Conectar Railway con GitHub |
| 6 | Railway despliega automáticamente |
| 7 | Acceder desde tablet con la URL |

---

## ✅ CHECKLIST FINAL

- [ ] Cuenta GitHub creada
- [ ] Repositorio GitHub creado
- [ ] Código subido a GitHub (`git push`)
- [ ] Cuenta Railway creada
- [ ] Proyecto conectado en Railway
- [ ] Railway muestra "Build Successful"
- [ ] Accediste desde navegador a la URL
- [ ] La tablet puede acceder

---

## 🆘 SI ALGO FALLA

### Error: "fatal: could not create work tree dir"
```bash
# Verifica que estés en la carpeta correcta
cd C:\Users\chomi\OneDrive\Practica\supermarket-mt
dir
```

### Error: "Permission denied (publickey)"
- GitHub → Settings → SSH and GPG keys
- Crea nuevo SSH key
- O usa "GitHub Desktop" (es más fácil)

### Error: "Build failed on Railway"
- Abre logs en Railway
- Busca qué error salió
- Revisa `requirements.txt`

---

## 💡 IMPORTANTE

- **La BD está en la nube ahora** (los datos se guardan allá)
- **Funciona 24/7** sin tu portátil
- **Acceso desde cualquier WiFi**
- **Gratis** (Railway da crédito gratuito)

---

## 🎉 ¡LISTO!

Tu app está en la nube. La tablet puede acceder desde el local.

---

## 📞 DATOS ÚTILES

- **URL de Railway Dashboard**: https://railway.app/dashboard
- **Estado de la app**: Railway → Deployments
- **Ver logs**: Railway → Deployments → Ver logs
- **Reiniciar app**: Railway → Redeploy

---

**¡Tu supermercado tiene sistema profesional en la nube! 🚀**
