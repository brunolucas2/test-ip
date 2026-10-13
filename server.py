from flask import Flask, request

app = Flask(__name__)

@app.before_request
def registrar():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    print(f"IP: {ip} | {request.method} {request.full_path}", flush=True)

@app.route("/")
def inicio():
    return "Servidor funcionando"