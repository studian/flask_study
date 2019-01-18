from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell():
    return "<h1>hellow world!</h1>"

if __name__ == '__main__':
    app.run()

