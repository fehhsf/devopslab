from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Alô Mundão v2"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)