from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import (
    init_db, add_product, get_product_by_barcode, get_all_products,
    update_product, delete_product, search_products, verify_admin, add_admin_user, change_admin_password
)
import os

app = Flask(__name__)
app.secret_key = 'supermarket_mt_2026_secure_key'

# Inicializar base de datos
if not os.path.exists('supermarket.db'):
    init_db()
    # Crear admin por defecto
    add_admin_user('admin', '1234')

@app.route('/')
def index():
    """Página principal - consultar precio"""
    return render_template('consultar.html')

@app.route('/api/search', methods=['POST'])
def search():
    """API para buscar productos por código de barras o nombre"""
    data = request.get_json()
    query = data.get('query', '').strip()
    
    if not query:
        return jsonify({'error': 'Búsqueda vacía'}), 400
    
    products = search_products(query)
    if products:
        return jsonify({
            'found': True,
            'products': [dict(p) for p in products]
        })
    else:
        return jsonify({'found': False}), 404

@app.route('/api/barcode', methods=['POST'])
def barcode_search():
    """API específica para búsqueda por código de barras"""
    data = request.get_json()
    barcode = data.get('barcode', '').strip()
    
    if not barcode:
        return jsonify({'error': 'Código de barras vacío'}), 400
    
    product = get_product_by_barcode(barcode)
    if product:
        return jsonify({
            'found': True,
            'product': dict(product)
        })
    else:
        return jsonify({'found': False}), 404

@app.route('/login_admin')
def login_admin():
    """Página de login para administrador"""
    return render_template('login_admin.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    """API para verificar credenciales de admin"""
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    if verify_admin(username, password):
        session['admin_logged_in'] = True
        session['username'] = username
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401

@app.route('/logout')
def logout():
    """Cerrar sesión de admin"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/api/change-password', methods=['POST'])
def change_password():
    """API para cambiar la contraseña del admin"""
    data = request.get_json()
    username = data.get('username', '')
    old_password = data.get('old_password', '')
    new_password = data.get('new_password', '')
    
    if not username or not new_password:
        return jsonify({'success': False, 'message': 'Datos incompletos'}), 400
    
    if len(new_password) < 4:
        return jsonify({'success': False, 'message': 'La contraseña debe tener mínimo 4 caracteres'}), 400
    
    if change_admin_password(username, old_password, new_password):
        return jsonify({'success': True, 'message': '✓ Contraseña cambiada exitosamente'})
    else:
        return jsonify({'success': False, 'message': 'Código actual incorrecto'}), 401

@app.route('/admin')
def admin():
    """Panel de administración"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('login_admin'))
    return render_template('admin.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    """API para obtener todos los productos (solo admin)"""
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'No autorizado'}), 401
    
    products = get_all_products()
    return jsonify([dict(p) for p in products])

@app.route('/api/products', methods=['POST'])
def add_new_product():
    """API para agregar un nuevo producto (solo admin)"""
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    barcode = data.get('barcode', '').strip()
    name = data.get('name', '').strip()
    price = data.get('price', 0)
    category = data.get('category', '').strip()
    
    if not barcode or not name:
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    if add_product(barcode, name, float(price), category):
        return jsonify({'success': True})
    else:
        return jsonify({'error': 'El código de barras ya existe'}), 409

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_existing_product(product_id):
    """API para actualizar un producto (solo admin)"""
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    name = data.get('name', '').strip()
    price = data.get('price', 0)
    category = data.get('category', '').strip()
    
    if not name:
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    update_product(product_id, name, float(price), category)
    return jsonify({'success': True})

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_existing_product(product_id):
    """API para eliminar un producto (solo admin)"""
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'No autorizado'}), 401
    
    delete_product(product_id)
    return jsonify({'success': True})

@app.route('/static/img/placeholder.svg')
def placeholder_image():
    """Sirve una imagen placeholder"""
    return '''
    <svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
        <rect width="200" height="200" fill="#e8f5e9"/>
        <text x="50%" y="50%" text-anchor="middle" dy=".3em" font-family="Arial" font-size="24" fill="#4caf50">
            Producto
        </text>
    </svg>
    ''', 200, {'Content-Type': 'image/svg+xml'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
