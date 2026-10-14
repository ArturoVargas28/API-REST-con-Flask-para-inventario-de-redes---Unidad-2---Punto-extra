from flask import Flask, jsonify

app = Flask('cabletrack_api_avv')

materiales = [
    {"id": 1, "nombre": "Cable UTP", "categoria": "cable", "unidad": "metros", "existencias": 40, "stock_minimo": 50},
    {"id": 2, "nombre": "Conector RJ45", "categoria": "conector", "unidad": "piezas", "existencias": 120, "stock_minimo": 100},
    {"id": 3, "nombre": "Pinzas", "categoria": "herramienta", "unidad": "piezas", "existencias": 3, "stock_minimo": 5},
    {"id": 4, "nombre": "Jack RJ45", "categoria": "conector", "unidad": "piezas", "existencias": 15, "stock_minimo": 20},
    {"id": 5, "nombre": "Cinchos", "categoria": "accesorio", "unidad": "paquetes", "existencias": 5, "stock_minimo": 10}
]

# 1. Estado de la API
@app.route('/')
def inicio():
    return "La API de CableTrack esta funcionando"

# 2. Ver todos
@app.route('/materiales')
def ver_todos():
    return jsonify(materiales)

# 3. Ver por id
@app.route('/materiales/<int:id_buscado>')
def ver_por_id(id_buscado):
    for m in materiales:
        if m["id"] == id_buscado:
            return jsonify(m)
    return jsonify({"error": "no encontrado"})

# 4. Ver por categoria
@app.route('/materiales/categoria/<cat>')
def ver_por_categoria(cat):
    lista = []
    for m in materiales:
        if m["categoria"] == cat:
            lista.append(m)
    return jsonify(lista)

# 5. Bajo stock
@app.route('/materiales/bajo-stock')
def bajo_stock():
    lista = []
    for m in materiales:
        if m["existencias"] <= m["stock_minimo"]:
            lista.append(m)
    return jsonify(lista)

app.run(debug=True)