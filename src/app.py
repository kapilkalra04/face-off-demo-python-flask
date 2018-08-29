from flask import Flask
import siameseTrain as ST1
import siameseTest as ST2
import siameseRecognizer as SR

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/train")
def train():
	return ST1.calculateTrainEmbeddings()


if __name__ == '__main__':
    app.run(debug=True)