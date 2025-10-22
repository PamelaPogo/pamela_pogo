from flask import Flask, jsonify, request
from calcular import suma

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "¡Aplicación de suma para examen DevOps",
        "status": "success", 
        "autor": "Moreno"
    })

@app.route('/health')
def health():
    return jsonify({"status": "OK", "service": "app-suma-moreno"})

@app.route('/sumar')
def sumar():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        resultado = suma(a, b)
        return jsonify({
            "operacion": "suma",
            "a": a,
            "b": b,
            "resultado": resultado
        })
    except ValueError:
        return jsonify({
            "error": "Los parámetros 'a' y 'b' deben ser números"
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)