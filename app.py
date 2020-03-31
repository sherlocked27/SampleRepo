from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def test1():
    print("Hello")
    print("Changes")
    return "hi"

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0" ,port=8888)
