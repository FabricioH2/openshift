from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def call_app_b():
    try:
        # Llamamos a la app B, que está en localhost:3001
        response = requests.get('http://route-occasional-iguana-ffisa-dev.apps.rm1.0a51.p1.openshiftapps.com/devCurso:4000/')
        return f'Respuesta de app B: {response.text}', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500

@app.route('/health', methods=['GET'])
def call_health():
    return 'OK', 200

@app.route('/startup', methods=['GET'])
def call_startup():
    return 'OK', 200
    
@app.route('/readiness', methods=['GET'])
def call_readiness():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)