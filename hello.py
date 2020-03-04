from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/foobar', methods=['GET'])
def foobar(params):
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#if __name__ == "__main__":
    #app.run(host='/127.0.0.1', port=5000)
    #app.run(debug=True)