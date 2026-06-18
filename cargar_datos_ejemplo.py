"""
Script para cargar datos de ejemplo en la base de datos
Ejecutar: python cargar_datos_ejemplo.py
"""

from database import init_db, add_product, add_admin_user

def load_demo_data():
    """Carga datos de ejemplo en la base de datos"""
    
    print("Inicializando base de datos...")
    init_db()
    
    print("Agregando usuario admin por defecto...")
    add_admin_user('admin', '1234')
    
    # Datos de ejemplo
    demo_products = [
        # Bebidas
        ('1234567890', 'Agua Mineral 500ml', 1.50, 'Bebidas'),
        ('1234567891', 'Jugo Natural Naranja 1L', 3.50, 'Bebidas'),
        ('1234567892', 'Coca-Cola 2L', 4.00, 'Bebidas'),
        ('1234567893', 'Leche Entera 1L', 2.80, 'Bebidas'),
        
        # Lácteos
        ('1234567894', 'Queso Blanco 500g', 8.50, 'Lácteos'),
        ('1234567895', 'Yogur Natural 250ml', 2.00, 'Lácteos'),
        ('1234567896', 'Mantequilla 250g', 6.00, 'Lácteos'),
        
        # Frutas y verduras
        ('1234567897', 'Manzanas por Kg', 5.50, 'Frutas'),
        ('1234567898', 'Plátanos por Kg', 2.50, 'Frutas'),
        ('1234567899', 'Tomates por Kg', 4.00, 'Verduras'),
        ('1234567900', 'Lechuga Fresca', 1.80, 'Verduras'),
        
        # Granos
        ('1234567901', 'Arroz 1kg', 3.50, 'Granos'),
        ('1234567902', 'Frijoles 1kg', 4.00, 'Granos'),
        ('1234567903', 'Harina Trigo 1kg', 2.50, 'Granos'),
        
        # Dulces
        ('1234567904', 'Chocolate 100g', 2.50, 'Dulces'),
        ('1234567905', 'Galletas Integrales 300g', 3.00, 'Dulces'),
        ('1234567906', 'Caramelos 100g', 1.50, 'Dulces'),
        
        # Productos de limpieza
        ('1234567907', 'Jabón Líquido 500ml', 3.50, 'Limpieza'),
        ('1234567908', 'Detergente Ropa 1kg', 5.50, 'Limpieza'),
        ('1234567909', 'Desinfectante 750ml', 4.00, 'Limpieza'),
        
        # Artículos de higiene
        ('1234567910', 'Papel Higiénico 4 rollos', 2.50, 'Higiene'),
        ('1234567911', 'Jabón de Baño 3 unidades', 3.50, 'Higiene'),
        ('1234567912', 'Pasta de Dientes 100g', 2.00, 'Higiene'),
    ]
    
    print("\nCargando productos de ejemplo...")
    count = 0
    for barcode, name, price, category in demo_products:
        if add_product(barcode, name, price, category):
            count += 1
            print(f"  ✓ {name} - ${price}")
        else:
            print(f"  ⚠ {name} (ya existe)")
    
    print(f"\n✓ Se cargaron {count} productos de ejemplo")
    print("\nCredenciales de admin:")
    print("  Usuario: admin")
    print("  PIN:     1234")
    print("\nAhora ejecuta: python app.py")

if __name__ == '__main__':
    load_demo_data()
