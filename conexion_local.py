from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)

    client.admin.command("ping")

    print("✅ Conexión exitosa a MongoDB Local.")

    db = client["ecommerce"]

    print("Base:", db.name)

except Exception as e:
    print("❌ Error:", e)