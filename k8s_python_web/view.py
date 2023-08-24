from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    server_name = os.uname()[1]
    return f"""
            <h1>Greetings!</h1>
            <p>This server is answering from pod:</p>
            <p>{server_name}</p>
            """

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)