from flask import Flask
from flask import request
import base64
import siameseTrain as ST1
import siameseTest as ST2
import siameseRecognizer as SR

app = Flask(__name__)

@app.route("/")
def hello():
    return "Connection Successful"

@app.route("/upload", methods=['POST'])
def upload():
	base64Data = request.form.get('imageData')
	empCount = request.form.get('empCount')
	with open("data/library/train2/"+ str(empCount) + ".jpeg", "wb") as fh:
		fh.write(base64.b64decode(base64Data))
	
	return "Data Received"
	
@app.route("/train",methods=['GET'])
def train():
	ST1.calculateTrainEmbeddings();
	return "Repository Embeddings Generated"

@app.route("/verify", methods=['POST'])
def verify():
	base64Data = request.form.get('imageData')
	with open("data/library/test2/" + "test.jpeg", "wb") as fh:
		fh.write(base64.b64decode(base64Data))
	ST2.calculateTestEmbeddings();
	norm = SR.calculateNorm();

	return str(norm)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)