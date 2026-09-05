from pymongo import MongoClient
import urllib.parse

# ⚠️ REEMPLAZA CON TUS CREDENCIALES

# Codificar caracteres especiales en la contraseña


# Cadena de conexión
connection_string = f"mongodb+srv://jupagaso_db_user:jpablo96@cluster1.mmizm3d.mongodb.net/"

try:
    client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
    
    # Verificar conexión
    client.admin.command("ping")
    
    print("✅ Conexión exitosa a MongoDB Atlas.")
    
    # Acceder a la base de datos
    db = client["ecommerce"]  # Cambia por tu nombre de BD
    
    print(f"Base de datos: {db.name}")
    
    # Ver colecciones
    collections = db.list_collection_names()
    print(f"Colecciones: {collections}")

except Exception as e:
    print(f"❌ Error de conexión: {e}")
    print("\n💡 Soluciones:")
    print("1. Verifica que el usuario y contraseña sean correctos")
    print("2. La contraseña puede contener caracteres especiales - intenta sin ellos")
    print("3. Asegúrate de que tu IP esté en el whitelist de Atlas")
    print("4. Verifica que la base de datos existe y que el usuario tiene permisos")
