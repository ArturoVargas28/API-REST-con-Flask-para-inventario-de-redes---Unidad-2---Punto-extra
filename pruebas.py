import urllib.request
import json

url = "http://127.0.0.1:5000/materiales/bajo-stock"

try:
    # Realiza la petición GET usando solo librerías que vienen instaladas por defecto en Python
    with urllib.request.urlopen(url) as respuesta:
        codigo = respuesta.getcode()
        print("Código de estado:", codigo)
        
        # Lee y decodifica el JSON de la respuesta
        datos = json.loads(respuesta.read().decode())
        
        print("\nMateriales que requieren reabastecimiento:")
        for m in datos:
            print("-", m["nombre"], "| Existencias:", m["existencias"])

except Exception as e:
    print("Error: No se pudo conectar a la API. Asegúrate de que 'app.py' esté ejecutándose en otra terminal.")
    print("Detalle:", e)