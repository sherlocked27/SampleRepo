from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def test1():
    print("Hello")
    print("Changes")
    print("One more change")
    print("Kisi aur ke changes")
    return "hi"

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0" ,port=8888)
