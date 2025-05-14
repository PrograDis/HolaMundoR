import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<h1>Hola desde Railway</h1>
<p>"El que tenga miedo a morir que no nazca" – Balazo</p>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
