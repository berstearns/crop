from flask import Flask, render_template, request, jsonify
import base64
import io
import pytesseract
from PIL import Image

app = Flask(__name__)


@app.route("/",methods=["GET"])
def index():
    return render_template("crop.html")

@app.route("/",methods=["POST"])
def process_canvas():
    base64_string = request.form["base64"]
    print(base64_string,file=open("dummy","w"))
    header, imgdata = base64_string.split(",",1)
    imgdata = base64.b64decode(imgdata)
    image = Image.open(io.BytesIO(imgdata))
    text = pytesseract.image_to_string(image)
    print(text)
    return jsonify({
        "text":text,
        "message":"success"
        }) 

if __name__ == "__main__":
    app.run(port=8002, debug=True)
