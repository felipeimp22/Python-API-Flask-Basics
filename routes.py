from flask import Flask, request
from main import getBody

app = Flask("Crud")

@app.route("/healthCheck", methods=["GET"])
def healthCheck():
    return {"message":"api is running"}

@app.route("/post", methods=["POST"])
def postFnc():
    body = request.get_json()
    # desestruturar:
    # exemplo: body["name"]
    
    if("name" not in body):
        return {"message":"name is missing!!!!"}
    
    ret = getBody(body)
    return ret


app.run()