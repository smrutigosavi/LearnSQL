from flask import Flask
app = Flask(__name__)

@app.route('/hello/<pavan>')
def hello_world():
    return f'Hello, {pavan}!'

if __name__ == '__main__':
    app.run()