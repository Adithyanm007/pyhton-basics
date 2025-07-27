from flask import Flask, jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return jsonify({"message":"Welcome to the first API"})
@app.route('/square/<int:num>')
def square(num):
    return jsonify({"number": num, "square": num ** 2})
if __name__ == '__main__':
    app.run(debug=True)