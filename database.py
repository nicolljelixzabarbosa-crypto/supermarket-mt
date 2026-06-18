import sqlite3
import os
from datetime import datetime

DATABASE = 'supermarket.db'

def get_db_connection():
    """Conecta a la base de datos SQLite"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa la base de datos con las tablas necesarias"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Tabla de productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabla de usuarios (admins y empleados)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def add_admin_user(username, password):
    """Agrega un usuario administrador"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
            (username, password, 'admin')
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_product_by_barcode(barcode):
    """Obtiene un producto por código de barras"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE barcode = ?', (barcode,))
    product = cursor.fetchone()
    conn.close()
    return product

def get_all_products():
    """Obtiene todos los productos"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products ORDER BY name')
    products = cursor.fetchall()
    conn.close()
    return products

def add_product(barcode, name, price, category):
    """Agrega un nuevo producto"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO products (barcode, name, price, category) VALUES (?, ?, ?, ?)',
            (barcode, name, price, category)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def update_product(product_id, name, price, category):
    """Actualiza un producto existente"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE products SET name = ?, price = ?, category = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?',
        (name, price, category, product_id)
    )
    conn.commit()
    conn.close()

def delete_product(product_id):
    """Elimina un producto"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

def search_products(query):
    """Busca productos por nombre o código de barras"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM products WHERE name LIKE ? OR barcode LIKE ? ORDER BY name',
        (f'%{query}%', f'%{query}%')
    )
    products = cursor.fetchall()
    conn.close()
    return products

def verify_admin(username, password):
    """Verifica credenciales de administrador"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ? AND role = ?', 
                   (username, password, 'admin'))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def change_admin_password(username, old_password, new_password):
    """Cambia la contraseña del admin después de verificar la actual"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificar que la contraseña actual es correcta
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ? AND role = ?', 
                   (username, old_password, 'admin'))
    user = cursor.fetchone()
    
    if user is None:
        conn.close()
        return False  # Contraseña actual incorrecta
    
    # Cambiar la contraseña
    cursor.execute(
        'UPDATE users SET password = ? WHERE username = ? AND role = ?',
        (new_password, username, 'admin')
    )
    conn.commit()
    conn.close()
    return True
