"""
Script para cambiar la contraseña del administrador
Ejecutar: python cambiar_contraseña.py
"""

import sqlite3
import getpass
import os

DATABASE = 'supermarket.db'

def change_admin_password():
    """Cambia la contraseña de admin de forma segura"""
    
    print("\n" + "="*50)
    print("🔐 CAMBIAR CONTRASEÑA DE ADMIN")
    print("="*50 + "\n")
    
    # Pedir contraseña actual
    current_password = getpass.getpass("Contraseña actual (deja en blanco si es la primera vez): ")
    
    # Verificar contraseña actual
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    if current_password:
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ? AND role = ?', 
                      ('admin', current_password, 'admin'))
        if not cursor.fetchone():
            print("❌ Contraseña actual incorrecta")
            conn.close()
            return False
    
    # Pedir nueva contraseña
    print()
    new_password = getpass.getpass("Nueva contraseña: ")
    confirm_password = getpass.getpass("Confirmar nueva contraseña: ")
    
    if new_password != confirm_password:
        print("❌ Las contraseñas no coinciden")
        conn.close()
        return False
    
    if len(new_password) < 4:
        print("❌ La contraseña debe tener al menos 4 caracteres")
        conn.close()
        return False
    
    # Actualizar contraseña
    cursor.execute('UPDATE users SET password = ? WHERE username = ? AND role = ?', 
                  (new_password, 'admin', 'admin'))
    conn.commit()
    conn.close()
    
    print("\n✅ ¡Contraseña actualizada correctamente!")
    print("   Nueva contraseña: *" + "*" * (len(new_password) - 1))
    print("\nUsa esta contraseña para acceder al panel de admin\n")
    return True

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        print("❌ Base de datos no encontrada")
        print("   Ejecuta primero: python app.py")
        exit(1)
    
    change_admin_password()
